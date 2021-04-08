import { DataTableDirective } from 'angular-datatables';
import { Subject } from 'rxjs';
import { Component, OnInit, OnDestroy, ViewChild, ChangeDetectorRef } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { MutationResumen } from "../../../models/mutationresumen";
import Swal from 'sweetalert2/dist/sweetalert2';
import { faDna } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnDestroy, OnInit {
  public faDna = faDna;
  /*Datatable*/
  @ViewChild(DataTableDirective) dtElement: DataTableDirective;
  public dtOptions: DataTables.Settings = {};
  public dtTrigger: Subject<any> = new Subject();
  /*Controladores de filtros*/
  public effectsSelected: Array<string>;
  public vhlSelected: Array<string>;
  public effectsList: Array<string>;
  public vhlList: Array<string>;
  /*Data resumen*/
  public mutations: Array<MutationResumen>;
  
  public showStructure: Boolean;
  public plugin;
  constructor(
    private _mutationService: MutationService,
    private chRef: ChangeDetectorRef
  ){}
  ngOnInit(){
    this.showStructure = false;
    /*Se obtiene la data de estos 3 atributos*/
    this.getMutations();
    this.getEffects();
    this.getVHL();
    /*Configuración del datatable*/
    this.dtOptions = {
        paging : true,
        pagingType: 'full_numbers',
        pageLength: 8,
        lengthMenu : [8, 15, 30],
    };
  }
  ngOnDestroy(): void {
    /*Recarga de datos*/
    this.dtTrigger.unsubscribe();
  }
  async ShowMutation(nombre, tipo, protein, dna){
    /*Popup que muestra las secuencias de ADN (opcional) y proteína de la mutación*/
    var html = ``
    if(dna!=undefined){
      dna = dna.toLowerCase();
      html += `<p style= "text-align: left; font-family: Ubuntu Mono; max-width: 60ch;">>Von Hippel Lindau Tumor Supressor CDS `+nombre+`<br>`+ dna + `</p>`
    }
    html += `<p style= "text-align: left; font-family: Ubuntu Mono; max-width: 60ch;">>pVHL `+nombre +`<br>`+ protein + `</p>`;
    if(tipo == "Missense"){
      let mutation = nombre.substring(2); 
      await this.getPdbExists(mutation);
      if(this.showStructure == true){
        html += `
        <mat-card id = "wrapper">
          <div id="structure" style = "position: relative; width: 98%; height: 415px; margin-left: 1%;">
          </div>
        </mat-card>`
      }
    }
    Swal.fire({
      width: 600,
      title: nombre,
      html: html,
      allowEscapeKey: true,
      allowOutsideClick: true,
      showCancelButton: false,
      showConfirmButton: false,
      animation: false
    });
/*     if(this.showStructure == true){
      this.plugin = LiteMol.Plugin.create({
        target: '#structure',
        viewportBackground: 'black',
        layoutState: {
            isExpanded: false,
            hideControls: true
        },
      });
      let mutation = nombre.substring(2); 
      this.plugin.loadMolecule({
          id: '1lm8 ' + mutation,
          url: 'http://localhost:3800/api/getPdb/' + mutation,
          format: 'pdb' // default
      });

    } */
  }
  actualizar(): void {
    /*Actualiza el datatable cuando hay cambios*/
    this.dtElement.dtInstance.then((dtInstance: DataTables.Api)=>{
      dtInstance.destroy();
      this.dtTrigger.next();
    });
  }
  async getMutations(){
    /*Obtiene y representa el resumen de las mutaciones */
    let temp = await this._mutationService.getMutations().toPromise();
    this.mutations = temp.mutation;
    this.chRef.detectChanges();
    this.dtTrigger.next();
  }
  async getEffects(){
    /*Obtiene todos los efectos de la base de datos*/
    let temp = await this._mutationService.getEffects().toPromise();
    this.effectsList = temp.effects;
  }
  async getVHL(){
    /*Obtiene todos los tipos de vhl de la base de datos*/
    let temp = await this._mutationService.getVHL().toPromise();
    this.vhlList = temp.vhls;
  }
  async find(){
    /*Aplica los filtros especificados y actualiza el datatable.*/
    let temp = await this._mutationService.getMutationsbyFilters(this.vhlSelected, this.effectsSelected).toPromise();
    this.mutations = temp.mutations;
    this.actualizar();
  }
  DownloadJSON(){
    /*Descarga en formato JSON*/
    this._mutationService.DownloadJSON("getAllJson");
  }
  DownloadCSV(){
    /*Descarga en formato CSV*/
    this._mutationService.DownloadCSV("getAll");
  }
  DownloadFasta(){
    /*Descarga en formato Fasta*/
    this._mutationService.DownloadFasta("getFasta");
  }
  async getPdbExists(nombre){
    this.showStructure = false;
    let temp = await this._mutationService.getPdbExists(nombre).toPromise();
    if(temp.message == "error"){
      this.showStructure = false;
    }
    else{
      this.showStructure = true;
    }
  }
}
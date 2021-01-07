import { DataTableDirective } from 'angular-datatables';
import { Subject } from 'rxjs';
import { Component, OnInit, OnDestroy, ViewChild, ChangeDetectorRef } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { MutationResumen } from "../../../models/mutationresumen";
import Swal from 'sweetalert2/dist/sweetalert2';
@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnDestroy, OnInit {
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
  constructor(
    private _mutationService: MutationService,
    private chRef: ChangeDetectorRef
  ){}
  ngOnInit(): void{
    /*Se obtiene la data de estos 3 atributos*/
    this.getMutations();
    this.getEffects();
    this.getVHL();
    /*Configuración del datatable*/
    this.dtOptions = {
        paging : true,
        pagingType: 'full_numbers',
        pageLength: 10,
        lengthMenu : [10, 25, 50],
    };
  }
  ngOnDestroy(): void {
    /*Recarga de datos*/
    this.dtTrigger.unsubscribe();
  }
  Legend(){
    /*Popup de texto informativo*/
    let popup_html = document.getElementById("popup_legend").innerHTML
    Swal.fire({
      title: "Field description",
      width: 1000,
      padding: 10,
      html: popup_html,
      allowEscapeKey: true,
      allowOutsideClick: true,
    });  
  }
  ShowMutation(nombre, protein, dna){
    /*Popup que muestra las secuencias de ADN (opcional) y proteína de la mutación*/
    var html = ``
    if(dna!=undefined){
      dna = dna.toLowerCase();
      html += `<p style= "text-align: left; font-family: Ubuntu Mono; max-width: 60ch;">>Von Hippel Lindau Tumor Supressor CDS `+nombre+`<br>`+ dna + `</p>`
    }
    html += `<p style= "text-align: left; font-family: Ubuntu Mono; max-width: 60ch;">>pVHL `+nombre +`<br>`+ protein + `</p>`;
    Swal.fire({
      width: 600,
      title: "Sequences",
      html: html,
      allowEscapeKey: true,
      allowOutsideClick: true,
      showCancelButton: false,
      showConfirmButton: false
    });  
  }
  actualizar(): void {
    /*Actualiza el datatable cuando hay cambios*/
    this.dtElement.dtInstance.then((dtInstance: DataTables.Api)=>{
      dtInstance.destroy();
      this.dtTrigger.next();
    });
  }
  getMutations(){
    /*Obtiene y representa el resumen de las mutaciones */
    this._mutationService.getMutations().subscribe(
      response=>{
        this.mutations = response.mutation;
        this.chRef.detectChanges();
        this.dtTrigger.next();
      }
    )
  }
  getEffects(){
    /*Obtiene todos los efectos de la base de datos*/
    this._mutationService.getEffects().subscribe(
      response=>{
        this.effectsList = response.effects;
      }
    ) 
  }
  getVHL(){
    /*Obtiene todos los tipos de vhl de la base de datos*/
    this._mutationService.getVHL().subscribe(
      response=>{
        this.vhlList = response.vhls;
      }
    )
  }
  find(){
    /*Aplica los filtros especificados y actualiza el datatable.*/
    this._mutationService.getMutationsbyFilters(this.vhlSelected, this.effectsSelected).subscribe(
      response=>{
        console.log(response);
        this.mutations = response.mutaciones;
        this.actualizar();
      }
    )
  }
  DownloadJSON(){
    /*Descarga en formato JSON*/
    this._mutationService.DownloadJSON("getAll");
  }
  DownloadCSV(){
    /*Descarga en formato CSV*/
    this._mutationService.DownloadCSV("getAll");
  }
  DownloadFasta(){
    /*Descarga en formato Fasta*/
    this._mutationService.DownloadFasta("getFasta");
  }
}
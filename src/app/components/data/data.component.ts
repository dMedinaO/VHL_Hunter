import { HttpClient } from '@angular/common/http';
import { DataTableDirective } from 'angular-datatables';
import { Subject } from 'rxjs';
import { Component, OnInit, AfterViewInit, OnDestroy, ViewChild, ChangeDetectorRef } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { MutationResumen } from "../../../models/mutationresumen";
@Component({
  selector: 'app-data',
  templateUrl: './data.component.html',
  styleUrls: ['./data.component.css']
})
export class DataComponent implements OnDestroy, OnInit {
  @ViewChild(DataTableDirective) dtElement: DataTableDirective;
  public dtOptions: DataTables.Settings = {};
  public dtTrigger: Subject<any> = new Subject();
  public title = 'VHL-Hunter';
  public mutations: Array<MutationResumen>;
  public effects: Array<string>
  public vhl: Array<string>
  public effSelected: string;
  public vhlSelected: string;
  constructor(
    private _mutationService: MutationService,
    private chRef: ChangeDetectorRef
  ){}
  ngOnInit(): void{
    this.getMutations();
    this.getEffects();
    this.getVHL();
    this.dtOptions = {
        paging : true,
        pagingType: 'full_numbers',
        pageLength: 10,
        lengthMenu : [10, 25, 50],
    };
  }
  ngOnDestroy(): void {
    this.dtTrigger.unsubscribe();
  }
  actualizar(): void {
    this.dtElement.dtInstance.then((dtInstance: DataTables.Api)=>{
      dtInstance.destroy();
      this.dtTrigger.next();
    });
  }
  getMutations(){
    this._mutationService.getMutations().subscribe(
      response=>{
        this.mutations = response.mutation;
        this.chRef.detectChanges();
        this.dtTrigger.next();
      },
      error =>{
        console.log("Error");
      }
    )
  }
  getEffects(){
    this._mutationService.getEffects().subscribe(
      response=>{
        let pre = ["All"]
        this.effects = pre.concat(response.effects);
      },
      error=>{
        console.log("Error");
      }
    )
  }
  getVHL(){
    this._mutationService.getVHL().subscribe(
      response=>{
        let pre = ["All"]
        this.vhl = pre.concat(response.vhls);
      },
      error=>{
        console.log("Error");
      }
    )
  }
  find(){
    if((this.effSelected == "All" && this.vhlSelected == undefined) || 
      (this.vhlSelected == "All" && this.effSelected == undefined) || 
      (this.vhlSelected == "All" && this.effSelected == "All")){
      this._mutationService.getMutations().subscribe(
        response=>{
          this.mutations = response.mutation;
          this.actualizar();
        },
        error =>{
          console.log("Error");
        }
      )
    }
    else{
      if((this.vhlSelected == undefined || this.vhlSelected == "All") && this.effSelected != undefined){
        this.getMutationsbyEffect();
      }
      else{
        if((this.effSelected == undefined || this.effSelected == "All") && this.vhlSelected != undefined){
          this.getMutationsbyVHL();
        }
        else{
          if(this.effSelected != undefined && this.vhlSelected != undefined){
            this.getMutationsbyBoth();
          }
        }
      }
    }
    
    
    
    

  }
  getMutationsbyEffect(){
    this._mutationService.getMutationsbyEffect(this.effSelected).subscribe(
      response=>{
        this.mutations = response.mutation;
        this.actualizar()
        for(var i =0;i<this.mutations.length; i++){
          try{
            this.mutations[i].Reports = response.mutation[i].Case.length;
          }
          catch{
            this.mutations[i].Reports = 0; 
          }
        }
      },
      error=>{
        console.log("Error");
      }
    )
  }
  getMutationsbyVHL(){
    this._mutationService.getMutationsbyVHL(this.vhlSelected).subscribe(
      response=>{
        this.mutations = response.mutations;
        this.actualizar()
        for(var i =0;i<this.mutations.length; i++){
            this.mutations[i].Reports = response.mutations[i].Case.length;            
        }
      },
      error=>{
        console.log("Error");
      }
    )
  }
  getMutationsbyBoth(){
    this._mutationService.getMutationbyBoth(this.vhlSelected, this.effSelected).subscribe(
      response=>{
        this.mutations = response.mutation;
        this.actualizar();
        for(var i =0;i<this.mutations.length; i++){
          this.mutations[i].Reports = response.mutation[i].Case.length;            
        }
      },
      error=>{
        console.log("Error");
        this.mutations = [];
        this.actualizar();
      }
    )
  }
}
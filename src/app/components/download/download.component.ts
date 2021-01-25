import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { HttpClient } from "@angular/common/http";
@Component({
  selector: 'app-download',
  templateUrl: './download.component.html',
  styleUrls: ['./download.component.css']
})
export class DownloadComponent implements OnInit {
  public types: Array<string>;
  public mutationTypeSelected: string;
  public moleculeSelected: string;
  public clinicalRiskSelected: string;
  public molecules = ["DNA", "Protein"];
  public clinicalRisk = ["High", "Low"];
  public effectsSelected: Array<string>;
  public vhlSelected: Array<string>;
  public effectsList: Array<string>;
  public vhlList: Array<string>;
  constructor(
    private _mutationService: MutationService,
    private http: HttpClient,
  ) { }
  ngOnInit(): void {
    this.getTypes();
    this.getEffects();
    this.getVHL();
  }
  getEffects(){
    this._mutationService.getEffects().subscribe(
      response=>{
        this.effectsList = response.effects;
      }
    )
  }
  getVHL(){
    this._mutationService.getVHL().subscribe(
      response=>{
        this.vhlList = response.vhls;
      }
    )
  }
  getTypes(){
    this._mutationService.getTypes().subscribe(
      response=>{
        this.types = response.types;
      }
    )
  }
  createUrl(){
    let vhl
    let eff
    let mutType
    let mol
    let risk
    if(this.vhlSelected == undefined){
        vhl = "undefined"
    }
    else{
        if(this.vhlSelected.length == 0){
            vhl = "undefined"
        }
        else{
            vhl = this.vhlSelected
        }
    }
    if(this.effectsSelected == undefined){
        eff = "undefined";
    }
    else{
        if(this.effectsSelected.length == 0){
            eff = "undefined";
        }
        else{
            eff = this.effectsSelected;
        }
    }
    if(this.mutationTypeSelected == undefined){
        mutType = "undefined";
    }
    else{
        mutType = this.mutationTypeSelected;
    }
    if(this.moleculeSelected == undefined){
        mol = "undefined";
    }
    else{
        mol = this.moleculeSelected;
    }
    if(this.clinicalRiskSelected == undefined){
      risk = "undefined";
    }
    else{
      if(this.clinicalRiskSelected == "High"){
        risk = "HIGH"
      }
      else{
        risk = "LOW"
      }
    }
    let url = "getDownloadsbyFilters/" + vhl + "/" + eff + "/" + mutType + "/" + mol + "/" + risk;
    return url;
  }
  DownloadCSV(){
    let url = this.createUrl()
    this._mutationService.DownloadCSV(url)
  }
  DownloadJSON(){
    let url = this.createUrl()
    this._mutationService.DownloadJSON(url);
  }
  DownloadFasta(){
    let url = this.createUrl()
    this._mutationService.DownloadFasta(url);
  }
}

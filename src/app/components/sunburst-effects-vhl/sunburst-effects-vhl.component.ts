import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { Mutation } from "../../../models/mutation";
@Component({
  selector: 'app-sunburst-effects-vhl',
  templateUrl: './sunburst-effects-vhl.component.html',
  styleUrls: ['./sunburst-effects-vhl.component.css']
})
export class SunburstEffectsVHLComponent implements OnInit {
  public mutations: Array<Mutation>
  public molecules
  public vhlTypes: Array<String>
  public effects: Array<String>
  public mutationTypes: Array<String>
  public data
  public layout
  constructor(
      private _mutationService: MutationService) { }
  async ngOnInit() {
      this.molecules = ["DNA", "Protein"]
      this.mutations = await this.getMutations()
      this.mutationTypes = await this.getTypes()
      this.vhlTypes = await this.getVHL()
      this.effects = await this.getEffects()
      this.data = await this.buildData()
      this.toPlotly()
  }
  getMutations(){
      return this._mutationService.getMutations().toPromise();
  }
  getVHL(){
      return this._mutationService.getVHL().toPromise();
  }
  getEffects(){
      return this._mutationService.getEffects().toPromise();
  }
  getTypes(){
      return this._mutationService.getTypes().toPromise();
  }  
  createUrl(url, VHL, EFF, MUTTYPE, MOL, RISK){
      let vhl
      let eff
      let mutType
      let mol
      let risk
      if(VHL == undefined){
          vhl = "undefined"
      }
      else{
          if(VHL.length == 0){
              vhl = "undefined"
          }
          else{
              vhl = VHL
          }
      }
      if(EFF == undefined){
          eff = "undefined";
      }
      else{
          if(EFF.length == 0){
              eff = "undefined";
          }
          else{
              eff = EFF;
          }
      }
      if(MUTTYPE == undefined){
          mutType = "undefined";
      }
      else{
          mutType = MUTTYPE;
      }
      if(MOL == undefined){
          mol = "undefined";
      }
      else{
          mol = MOL;
      }
      if(RISK == undefined){
      risk = "undefined";
      }
      else{
          if(RISK == "High"){
              risk = "HIGH"
          }
          else{
              risk = "LOW"
          }
      }
      let new_url = url + vhl + "/" + eff + "/" + mutType + "/" + mol + "/" + risk;
      return new_url;
  }
  async buildData(){
    let efftemp = this.effects["effects"]
    let vhltemp = this.vhlTypes["vhls"]
    let arr = []
    for(var vhl = 0; vhl < vhltemp.length; vhl++){
      let arr2 = []
      for(var eff = 0; eff < efftemp.length; eff++){
        let url = this.createUrl("getNumberbyFilters/", vhltemp[vhl], efftemp[eff], undefined, undefined, undefined)
        let number
        number = await this._mutationService.getNumberbyFilters(url).toPromise()
        arr2.push({"name": efftemp[eff], "number": number.cant})
      }
      for(let x = 0; x < arr2.length; x++){
        if(arr2[x].number == 0){
          arr2.splice(x, 1)
          x -=1
        }
      }
      arr.push({"name": vhltemp[vhl], "children": arr2})
    }
    for(let x = 0; x < arr.length; x++){
      if(arr[x].children.length == 0){
        arr.splice(x, 1)
        x -=1
      }
    }
    return {"name": "Mutations", "children": arr}
  }
  toPlotly(){
      var ids = []
      var labels = []
      var values = []
      var parents = []
      var data = this.data.children
      for(let i = 0; i<data.length; i++){
          let sum2 = 0
          var first = data[i].children
          if(first != undefined){
              for(let j = 0; j<first.length; j++){
                  ids.push(data[i].name+ " - " +first[j].name)
                  labels.push(first[j].name)
                  parents.push(data[i].name)
                  values.push(first[j].number)
                  sum2 += first[j].number
              }
          }
          ids.push(data[i].name)
          labels.push(data[i].name)
          parents.push("")
          values.push(sum2)
      }
      this.data = [
          {
              "type": "sunburst",
              "ids": ids,
              "labels": labels,
              "parents": parents,
              "values": values,
              "marker": {"line": {"width": 2}},
              "branchvalues": 'total'
          }
      ];
      this.layout = {
          margin: {l: 0, r: 0, b: 0, t:0},
          colorscale:'RdBu',
          width: 1200,
          height: 500
      };
  }
}

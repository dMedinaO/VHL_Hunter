import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import { Mutation } from "../../../models/mutation";
@Component({
    selector: 'app-sunburst-effects',
    templateUrl: './sunburst-effects.component.html',
})
export class SunburstEffectsComponent {
    public mutations: Array<Mutation>
    public molecules
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
        this.effects = await this.getEffects()
        this.data = await this.buildData()
        this.toPlotly()
    }
    getMutations(){
        return this._mutationService.getMutations().toPromise();
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
        let mutationTypeTemp = this.mutationTypes["types"]
        let moleculestemp = this.molecules
        let arr3 = []
        for(var mol = 0; mol < moleculestemp.length; mol++){
            let arr2 = []
        for(var mut = 0; mut < mutationTypeTemp.length; mut++){
            let arr = []
            for(var eff= 0; eff < efftemp.length; eff++){
                let url = this.createUrl("getNumberbyFilters/", undefined, efftemp[eff], mutationTypeTemp[mut], moleculestemp[mol], undefined)
                let number
                number = await this._mutationService.getNumberbyFilters(url).toPromise()
                arr.push({"name": efftemp[eff], "number": number.cant})
            }
            for(let x = 0; x < arr.length; x++){
                if(arr[x].number == 0){
                    arr.splice(x, 1)
                    x -=1
                }
            }
            arr2.push({"name": mutationTypeTemp[mut], "children": arr})
        }
        for(let x = 0; x < arr2.length; x++){
            if(arr2[x].children.length == 0){
                arr2.splice(x, 1)
                x -=1
            }
        }
        arr3.push({"name": moleculestemp[mol], "children": arr2})
        }
        return {"name": "Effects", "children": arr3}
    }
    toPlotly(){
        var ids = []
        var labels = []
        var values = []
        var parents = []
        var data = this.data.children
        for(let i = 0; i<data.length; i++){
            let sum2 = 0
            var molecule = data[i].children
            if(molecule != undefined){
                for(let j = 0; j<molecule.length; j++){
                    var mutType = molecule[j].children
                    let sum = 0
                    if(mutType != undefined){
                        for(let k = 0; k<mutType.length; k++){
                            ids.push(data[i].name + " - " + molecule[j].name + " - " + mutType[k].name)
                            labels.push(mutType[k].name)
                            values.push(mutType[k].number)
                            parents.push(data[i].name + " - " + molecule[j].name)
                            sum += mutType[k].number
                        }
                    }
                    ids.push(data[i].name+ " - " +molecule[j].name)
                    labels.push(molecule[j].name)
                    parents.push(data[i].name)
                    values.push(sum)
                    sum2 += sum
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
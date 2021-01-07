import {Injectable} from "@angular/core";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/Observable";
import {Global} from "./global";
import { saveAs } from '../../node_modules/file-saver';
@Injectable()
export class MutationService{
    public url: string;
    constructor(
        private _http: HttpClient
    ){
        this.url = Global.url;
    }
    getMutations(): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getMutations", {headers: headers});
    }
    getMutation(mutation: string): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getMutation/" + mutation, {headers: headers});
    }
    getEffects(): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getEffectsTotal", {headers: headers});
    }
    getVHL(): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getVHLTotal", {headers: headers});
    }
    getMutationsbyEffect(effect: string): Observable <any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getMutationsbyEffect/" + effect, {headers: headers});
    }
    getMutationsbyVHL(vhl: string): Observable <any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getMutationsbyVHL/" + vhl, {headers: headers});
    }
    getMutationbyBoth(vhl: string, effect: string): Observable <any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getMutationsbyBoth/" + vhl + "/" + effect, {headers: headers});
    }
    getTypes(): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get(this.url + "getTypesTotal", {headers: headers});
    }
    getMutationsbyFilters(vhlTypes:string[], effects:string[]):Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        this.url = Global.url
        let vhl
        let eff
        if(vhlTypes == undefined){
            vhl = "undefined"
        }
        else{
            if(vhlTypes.length == 0){
                vhl = "undefined"
            }
            else{
                vhl = vhlTypes
            }
        }
        if(effects == undefined){
            eff = "undefined";
        }
        else{
            if(effects.length == 0){
                eff = "undefined";
            }
            else{
                eff = effects;
            }
        }
        this.url += "getMutationsbyFilters/" + vhl + "/" + eff;
        return this._http.get(this.url, {headers: headers});
    }
    DownloadJSON(url:string){
        this.url = Global.url + url
        this._http.get<any>(this.url, {responseType: 'blob' as 'json'})
          .subscribe((res) => {
            saveAs(res, "VHLHunterData.json")
          })
    }
    DownloadCSV(url:string){
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        this.url = Global.url + url
        var text = `Mutation;Mutation_type;Molecule;VHL_types;Effects;DNA_sequence;Protein_sequence\n`;
        this._http.get(this.url, {headers:headers})
        .subscribe((res) => {
            console.log(res)
        for(var i = 0; i< res["mutation"].length;i++){
            var mutacion = res["mutation"][i];
            var efectos = []
            var vhltypes = []
            var cases = mutacion["Case"]
            if(cases!= undefined){
            for(var j=0; j<cases.length; j++){
                var c = cases[j]
                if(c["VHL_type"] != undefined && !vhltypes.includes(c["VHL_type"])){
                vhltypes.push(c["VHL_type"])
                }
                if(c["Disease"] != undefined){
                for(var k = 0; k < c["Disease"].length; k++){
                    if(c["Disease"][k]["Effect"] != undefined && !efectos.includes(c["Disease"][k]["Effect"]))
                    efectos.push(c["Disease"][k]["Effect"])
                }
                }
            }
            }
            text += mutacion["Mutation"] + `;` + mutacion["Mutation_type"] + `;` + mutacion["Molecule"] + `;`
            + vhltypes.toString() + `;` + efectos.toString() + `;`;
            if(mutacion["DNA_sequencee"] != undefined){
            text += mutacion["DNA_sequence"] + `;`
            }
            text += mutacion["Protein_sequence"] + `\n`
        }
        var file = new Blob([text], {type: "text/plain"});
        saveAs(file, "VHLHunterData.csv");
        })
    }
    DownloadFasta(url:string){
        this.url = Global.url + url
        var text = ``;
        this._http.get(this.url)
        .subscribe((res) => {
        for(var i = 0; i< res["mutation"].length; i++){
            text += `>`+ res["mutation"][i].Mutation + `\n`
            text += res["mutation"][i].Protein_sequence + `\n`
        }
        var file = new Blob([text], {type: "text/plain"});
        saveAs(file, "VHLHunter_FullData.fasta");
        })       
    }
}
import {Injectable} from "@angular/core";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/Observable";
import {MutationResumen} from "../models/mutationresumen";
import {Global} from "./global";
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
}
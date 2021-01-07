import {Injectable} from "@angular/core";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/Observable";
@Injectable()
export class PapersService{
    constructor(
        private _http: HttpClient
    ){
    }
    getPaper(url): Observable<any>{
        let headers = new HttpHeaders().set("Content-Type", "application/json");
        return this._http.get("" + url, {headers: headers});
    }
}
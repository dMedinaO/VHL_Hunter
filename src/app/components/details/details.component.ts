import { Component, OnInit, AfterViewInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { MutationService } from "../../../services/mutation.service";
import { MutationCases } from "../../../models/mutationcases";
@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent implements OnInit {
  public mutation:string;
  public title:string;
  public mutationCase: MutationCases;
  public dtOptions2: any = {};
  constructor(private rutaActiva: ActivatedRoute, 
    private _mutationService: MutationService) {
   }
  ngOnInit(): void {
    this.mutation = this.rutaActiva.snapshot.params.mutation;
    this.title = this.mutation;
    this.getMutation(this.mutation);
    this.dtOptions2 = {
      paging : false,
      pagingType: 'full_numbers',
      processing: false,
      searching : false,
      info: false, 
      ordering: false,
      language: {
        emptyTable: "No effects"
      }
    };
  }
  getMutation(mutation:string){
    this._mutationService.getMutation(mutation).subscribe(
      response=>{
        this.mutationCase = response.mutation[0]
        console.log(this.mutationCase);
      },
      error=>{
        console.log("Error");
      }
    )
  }
}
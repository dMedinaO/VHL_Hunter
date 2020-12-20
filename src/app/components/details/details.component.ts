import { Component, OnInit } from '@angular/core';
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
  public dataReady: boolean = false;
  constructor(private rutaActiva: ActivatedRoute, private _mutationService: MutationService) { }
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
        this.mutationCase = response.mutation[0];
        if(this.mutationCase.Mutation_type.includes("(nt)")){
          this.mutationCase.Molecule = "DNA";
        }
        else{
          this.mutationCase.Molecule = "Protein";
        }
        this.mutationCase.Mutation_type = this.mutationCase.Mutation_type.
        replace(" (nt)", "").replace("(aa)", "").replace("_", " ");
        console.log(this.mutationCase);
        this.dataReady = true;
      },
      error=>{
        console.log("Error");
      }
    )
  }
}
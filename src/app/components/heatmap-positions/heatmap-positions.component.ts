import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";

@Component({
  selector: 'app-heatmap-positions',
  templateUrl: './heatmap-positions.component.html',
  styleUrls: ['./heatmap-positions.component.css']
})
export class HeatmapPositionsComponent implements OnInit {
  public aminoacids: Array<String>
  public matriz: Array<Array<number>>
  public sequence: String;
  public xlabel: Array<String>
  public data
  public layout
  constructor(
    private _mutationService: MutationService)  { }
  async ngOnInit() {
    let temp = await this.getMutations()
    this.matriz = temp.data;
    this.aminoacids = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    temp = await this.getSequence();
    this.sequence = temp.sequence.split("");
    this.xlabel = []
    for(let i = 0; i<this.sequence.length; i++){
      let label = await (i+1).toString() +" "+this.sequence[i]
      this.xlabel.push(label)
    }
    this.buildData()
    this.layout = {
      xaxis: {
        type: "category",
        side: 'bottom',
        title: {
          text: 'pVHL Sequence',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
        automargin: false
      },
      yaxis: {
        side: 'top',
        title: {
          text: 'Mutated aminoacid',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
        automargin: true
      },
      width: 1200,
      height: 500,
    }
  }
  getMutations(){
    return this._mutationService.getSubstitutionPosition().toPromise();
  }
  getSequence(){
    return this._mutationService.getProteinSequence().toPromise();
  }
  buildData(){
    this.data = [{
      showscale: false,
      z : this.matriz,
      x : this.xlabel,
      y : this.aminoacids,
      type: "heatmap",
      colorscale: [
        [0, 'rgb(255, 255, 255)'],
        [1, 'rgb(0, 0, 200)'],
      ]
      }]
  }
}

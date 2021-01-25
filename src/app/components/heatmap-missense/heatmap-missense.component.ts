import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
@Component({
  selector: 'app-heatmap-missense',
  templateUrl: './heatmap-missense.component.html',
  styleUrls: ['./heatmap-missense.component.css']
})
export class HeatmapMissenseComponent implements OnInit {
  public aminoacids: Array<String>
  public matriz: Array<Array<number>>
  public data
  public layout
  constructor(
    private _mutationService: MutationService)  { }
  async ngOnInit() {
    let temp = await this.getMutations()
    this.matriz = temp.data;
    this.aminoacids = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    this.buildData()
    this.layout = {
      xaxis: {
        side: 'top',
        title: {
          text: 'Mutated aminoacid',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
      },
      yaxis: {
        side: 'top',
        title: {
          text: 'Wild type aminoacid',
          font: {
            family: 'Courier New, monospace',
            size: 18,
            color: '#7f7f7f'
          }
        },
      },
      width: 1200,
      height: 500,
    }
  }
  getMutations(){
    return this._mutationService.getSubstitutionMatrix().toPromise();
  }
  buildData(){
    this.data = [{
      z : this.matriz,
      x : this.aminoacids,
      y : this.aminoacids,
      type: "heatmap",
      colorscale: [
        [0, 'rgb(255, 255, 255)'],
        [1, 'rgb(0, 0, 200)'],
      ]
      }
    ]
  }
}

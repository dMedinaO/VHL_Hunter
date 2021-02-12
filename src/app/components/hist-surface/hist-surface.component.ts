import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";

@Component({
  selector: 'app-hist-surface',
  templateUrl: './hist-surface.component.html',
  styleUrls: ['./hist-surface.component.css']
})
export class HistSurfaceComponent implements OnInit {
  public data
  public xlabel
  public sequence
  public layout
  constructor(
    private _mutationService: MutationService) { }
  async ngOnInit() {
    this.xlabel = ["A", "B", "C", "D", "N"]
    let temp2 = await this.getHist()
    this.data = [{
      x: this.xlabel,
      y: temp2.data[0],
      type: 'bar',
      marker: {
        color: ["#F28871", "#73A4BF", "#92D394", "#DAD372", "grey"]
      }
    }
  ]
  this.layout = {      
    xaxis: {
      side: 'bottom',
      title: {
        text: 'Surface',
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
        text: 'Number of mutations',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    },
      width: 1200,
      height: 500,
    }
  }
  getHist(){
    return this._mutationService.getVarSurface().toPromise();
  }
}
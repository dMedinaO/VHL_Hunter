import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";


@Component({
  selector: 'app-hist-vhl',
  templateUrl: './hist-vhl.component.html',
  styleUrls: ['./hist-vhl.component.css']
})
export class HistVHLComponent implements OnInit {
  public data
  public xlabel
  public sequence
  public layout
  constructor(
    private _mutationService: MutationService) { }
  async ngOnInit() {
    let temp = await this.getSequence();
    this.sequence = temp.sequence.split("");
    this.xlabel = []
    for(let i = 0; i<this.sequence.length; i++){
      let label = await (i+1).toString() +" "+this.sequence[i]
      this.xlabel.push(label)
    }
    let temp2 = await this.getHist()
    this.data = [{
      x: this.xlabel,
      y: temp2.data[0],
      type: 'bar',
      name : "1",
      marker: {
        color: "#F28871"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[1],
      type: 'bar',
      name : "2",
      marker: {
        color: "#73A4BF"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[2],
      type: 'bar',
      name : "2A",
      marker: {
        color: "#92D394"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[3],
      type: 'bar',
      name : "2B",
      marker: {
        color: "#DAD372"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[4],
      type: 'bar',
      name : "2C",
      marker: {
        color: "grey"
      }
    }
  ]
    this.layout = {
      xaxis: {
        side: 'bottom',
        title: {
          text: 'pVHL Sequence',
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
      barmode: "stack"
    }
  }
  getHist(){
    return this._mutationService.getHistVHL().toPromise();
  }
  getSequence(){
    return this._mutationService.getProteinSequence().toPromise();
  }
}
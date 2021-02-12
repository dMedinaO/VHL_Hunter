import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";

@Component({
  selector: 'app-histogram-positions',
  templateUrl: './histogram-positions.component.html',
  styleUrls: ['./histogram-positions.component.css']
})
export class HistogramPositionsComponent implements OnInit {
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
    let A = this.xlabel.slice(0,58);
    let Ay = temp2.data[0].slice(0,58);
    let B = this.xlabel.slice(59, 102);
    let By = temp2.data[0].slice(59,102);
    let C = this.xlabel.slice(103, 152);
    let Cy = temp2.data[0].slice(103,152);
    let D = this.xlabel.slice(153, 188); 
    let Dy = temp2.data[0].slice(153,188);
    let N = this.xlabel.slice(189, this.xlabel.length - 1);
    let Ny = temp2.data[0].slice(189, this.xlabel.length - 1);
    this.data = [{
      x: A,
      y: Ay,
      type: 'bar',
      name: "A",
      marker: {
        color: "#F28871"
      }
    },
    {
      x: B,
      y: By,
      type: 'bar',
      name: "B",
      marker: {
        color: "#73A4BF"
      }
    },
    {
      x: C,
      y: Cy,
      type: 'bar',
      name: "C",
      marker: {
        color: "#92D394"
      }
    },
    {
      x: D,
      y: Dy,
      type: 'bar',
      name: "D",
      marker: {
        color: "#DAD372"
      }
    },
    {
      x: N,
      y: Ny,
      type: 'bar',
      name: "N",
      marker: {
        color: "grey"
      }
    }
  ];
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
    }
  }
  getHist(){
    return this._mutationService.getHistPositions().toPromise();
  }
  getSequence(){
    return this._mutationService.getProteinSequence().toPromise();
  }
}
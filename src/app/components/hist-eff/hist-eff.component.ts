import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";

@Component({
  selector: 'app-hist-eff',
  templateUrl: './hist-eff.component.html',
  styleUrls: ['./hist-eff.component.css']
})
export class HistEffComponent implements OnInit {
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
    /*["Renal Cell Carcinoma", "Pheochromocytoma", "Hemangioblastoma", "Cyst Adenoma", "Angioma", "Adenocarcinoma"] */
    let temp2 = await this.getHist()
    console.log(temp2.data)
    this.data = [{
      x: this.xlabel,
      y: temp2.data[0],
      type: 'bar',
      name : "Renal Cell Carcinoma",
      marker: {
        color: "#F28871"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[1],
      type: 'bar',
      name : "Pheochromocytoma",
      marker: {
        color: "#73A4BF"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[2],
      type: 'bar',
      name : "Hemangioblastoma",
      marker: {
        color: "#92D394"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[3],
      type: 'bar',
      name : "Cyst Adenoma",
      marker: {
        color: "#DAD372"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[4],
      type: 'bar',
      name : "Angioma",
      marker: {
        color: "grey"
      }
    },
    {
      x: this.xlabel,
      y: temp2.data[5],
      type: 'bar',
      name : "Adenocarcinoma",
      marker: {
        color: "#f5b87f"
      }
    }
  ]
    this.layout = {
      width: 1200,
      height: 500,
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
      barmode: "stack"
    }
  }
  getHist(){
    return this._mutationService.getHistEff().toPromise();
  }
  getSequence(){
    return this._mutationService.getProteinSequence().toPromise();
  }
}
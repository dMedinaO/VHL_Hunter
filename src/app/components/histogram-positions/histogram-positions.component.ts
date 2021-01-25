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
    this.data = [{
      x: this.xlabel,
      y: temp2.data[0],
      type: 'bar',
      marker: {
        color: 'rgb(0, 0, 200)'
      }
    }]
    this.layout = {
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
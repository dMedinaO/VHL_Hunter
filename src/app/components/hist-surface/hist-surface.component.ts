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
    this.xlabel = ["A", "B", "C", "D"]
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
    return this._mutationService.getVarSurface().toPromise();
  }
}
import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import * as Highcharts from 'highcharts';
import HC_exporting from 'highcharts/modules/exporting';
HC_exporting(Highcharts);
import HC_more from 'highcharts/highcharts-more'
HC_more(Highcharts);
import HC_surkey from 'highcharts/modules/sankey';
HC_surkey(Highcharts)

@Component({
  selector: 'app-sankey-eff',
  templateUrl: './sankey-eff.component.html',
  styleUrls: ['./sankey-eff.component.css']
})
export class SankeyEffComponent implements OnInit {
  public data; 
  public nulos;
  public Highcharts: typeof Highcharts = Highcharts;
  public options;
  constructor(private _mutationService: MutationService) {}
  async ngOnInit(){
    let temp = await this.getEffData()
    this.data = temp["data"]
    for(var i = 0; i<this.data.length; i++){
      this.data[i][2] = parseInt(this.data[i][2], 10)
    }
    this.options = {
      series: [{
        type: 'sankey',
        keys: ['from', 'to', 'weight'],
        data: this.data
        }],
      title: {
        text: ''
      },
      chart: {
        width: 1200,
        height: 600,
      },
      credits: {enabled: false}
    };
  }
  getEffData(){
    return this._mutationService.getSankeyEff().toPromise();
  }
}
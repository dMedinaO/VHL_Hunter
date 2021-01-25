import { Component, OnInit } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
import * as Highcharts from 'highcharts';
import HC_exporting from 'highcharts/modules/exporting';
HC_exporting(Highcharts);
import HC_more from 'highcharts/highcharts-more'
HC_more(Highcharts);
import HC_venn from 'highcharts/modules/venn';
HC_venn(Highcharts)
@Component({
  selector: 'app-venn-vhl',
  templateUrl: './venn-vhl.component.html',
  styleUrls: ['./venn-vhl.component.css']
})
export class VennVHLComponent implements OnInit {
  public data; 
  public nulos;
  public Highcharts: typeof Highcharts = Highcharts;
  public options;
  constructor(private _mutationService: MutationService) { }
  async ngOnInit(){
    this.data = await this.getVHLVenn()
    for(let i = 0; i < this.data.data.length; i++){
      if(this.data.data[i].name == ""){
        this.nulos = this.data.data[i].value;
        delete this.data.data[i]
      }
    }
    this.options = {
      series: [{
        type: 'venn',
        data: this.data.data
        }],
      title: {
        text: ''
      }, 
      chart: {
        width: 1200,
        height: 500,
      },
      credits: {enabled: false}
    };
  }
  getVHLVenn(){
    return this._mutationService.getVHLVenn().toPromise();
  }
}
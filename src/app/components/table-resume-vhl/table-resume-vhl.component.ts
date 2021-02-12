import { DataTableDirective } from 'angular-datatables';
import { Subject } from 'rxjs';
import { Component, OnInit, OnDestroy, ViewChild, ChangeDetectorRef } from '@angular/core';
import { MutationService } from "../../../services/mutation.service";
@Component({
  selector: 'app-table-resume-vhl',
  templateUrl: './table-resume-vhl.component.html',
  styleUrls: ['./table-resume-vhl.component.css']
})
export class TableResumeVHLComponent implements OnInit {
  /*Datatable*/
  @ViewChild(DataTableDirective) dtElement: DataTableDirective;
  public dtOptions: DataTables.Settings = {};
  public dtTrigger: Subject<any> = new Subject();
  /*Controladores de filtros*/
  public data;
  public head;
  constructor(
    private _mutationService: MutationService,
    private chRef: ChangeDetectorRef) { }
  ngOnInit() {
    this.getResumeVHL();
    this.dtOptions = {
      paging : true,
      pagingType: 'full_numbers',
      processing: false,
      searching : true,
      info: false, 
      ordering: true,
      order: [[ 11, "desc" ]]
    };
  }
  getResumeVHL(){
    return this._mutationService.getResumeVHL().subscribe(
      response=>{
        this.data = []
        this.chRef.detectChanges();
        this.dtTrigger.next();
        let vhls = Object.keys(response.data)
        for(var i = 0; i<vhls.length; i++){
          let row = []
          row.push(vhls[i])
          let datitos = Object.values(response.data[vhls[i]])
          row = row.concat(datitos, datitos.reduce(this.getSum, 0))
          this.data.push(row)
        }
      }
    )
  }
  getSum(total, num) {
    return total + Math.round(num);
  }
  ngOnDestroy(): void {
    /*Recarga de datos*/
    this.dtTrigger.unsubscribe();
  }
  actualizar(): void {
    /*Actualiza el datatable cuando hay cambios*/
    this.dtElement.dtInstance.then((dtInstance: DataTables.Api)=>{
      dtInstance.destroy();
      this.dtTrigger.next();
    });
  }
}

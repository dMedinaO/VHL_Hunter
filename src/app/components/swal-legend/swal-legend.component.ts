import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2/dist/sweetalert2';

@Component({
  selector: 'app-swal-legend',
  templateUrl: './swal-legend.component.html',
  styleUrls: ['./swal-legend.component.css']
})
export class SwalLegendComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  Legend(){
    /*Popup de texto informativo*/
    let popup_html = document.getElementById("popup_legend").innerHTML
    Swal.fire({
      title: "Field description",
      width: 1000,
      padding: 10,
      html: popup_html,
      allowEscapeKey: true,
      allowOutsideClick: true,
      animation: false
    });  
  }
}

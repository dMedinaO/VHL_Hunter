import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { MutationService } from "../services/mutation.service";
import { MutationResumen } from "../models/mutationresumen";
import {Global} from "../services/global";
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MutationService]
})
export class AppComponent implements OnInit{
  public title = 'VHL-Hunter';
  constructor(
  ){}
  ngOnInit(){
  }
}
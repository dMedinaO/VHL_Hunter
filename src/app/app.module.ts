import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { routing, appRoutingProviders } from "./app.routing";
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { MatCard, MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatTabsModule } from '@angular/material/tabs';
import { DataTablesModule } from "angular-datatables";
import { HttpClientModule } from "@angular/common/http";
import { DetailsComponent } from './components/details/details.component';
import { DataComponent } from './components/data/data.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { DownloadComponent } from './components/download/download.component';
import { VisualizationComponent } from './components/visualization/visualization.component';
import * as PlotlyJS from 'plotly.js/dist/plotly.js';
import { PlotlyModule } from 'angular-plotly.js';
import { SunburstVHLComponent } from './components/sunburst-vhl/sunburst-vhl.component';
import { SunburstEffectsComponent } from './components/sunburst-effects/sunburst-effects.component';
import { HeatmapMissenseComponent } from './components/heatmap-missense/heatmap-missense.component';
import { SunburstEffectsVHLComponent } from './components/sunburst-effects-vhl/sunburst-effects-vhl.component';
import { HighchartsChartModule } from "highcharts-angular";
import { VennVHLComponent } from './components/venn-vhl/venn-vhl.component';
import { VennEffComponent } from './components/venn-eff/venn-eff.component';
import { HeatmapPositionsComponent } from './components/heatmap-positions/heatmap-positions.component';
import { SankeyVHLComponent } from './components/sankey-vhl/surkey-vhl.component';
import { HistogramPositionsComponent } from './components/histogram-positions/histogram-positions.component';
import { HistSurfaceComponent } from './components/hist-surface/hist-surface.component';
import { SankeyEffComponent } from './components/sankey-eff/sankey-eff.component';
import { HistVHLComponent } from './components/hist-vhl/hist-vhl.component';
import { HistEffComponent } from './components/hist-eff/hist-eff.component';
import { TableResumeVHLComponent } from './components/table-resume-vhl/table-resume-vhl.component';
import { TableResumeEffComponent } from './components/table-resume-eff/table-resume-eff.component';
PlotlyModule.plotlyjs = PlotlyJS;

@NgModule({
  declarations: [
    AppComponent,
    DetailsComponent,
    DataComponent,
    DownloadComponent,
    VisualizationComponent,
    SunburstVHLComponent,
    SunburstEffectsComponent,
    HeatmapMissenseComponent,
    SunburstEffectsVHLComponent,
    VennVHLComponent,
    VennEffComponent,
    HeatmapPositionsComponent,
    SankeyVHLComponent,
    HistogramPositionsComponent,
    HistSurfaceComponent,
    SankeyEffComponent,
    HistVHLComponent,
    HistEffComponent,
    TableResumeVHLComponent,
    TableResumeEffComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    FormsModule,
    MatInputModule,
    MatButtonModule,
    MatFormFieldModule,
    MatSelectModule,
    MatCardModule,
    MatIconModule,
    MatTabsModule,
    HttpClientModule,
    DataTablesModule,
    routing,
    BrowserAnimationsModule,
    PlotlyModule,
    HighchartsChartModule
  ],
  providers: [appRoutingProviders],
  bootstrap: [AppComponent]
})
export class AppModule { }

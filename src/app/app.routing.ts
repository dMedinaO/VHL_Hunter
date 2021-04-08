import { ModuleWithProviders } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { DetailsComponent } from './components/details/details.component';
import { DataComponent } from './components/data/data.component';
import { AppComponent } from "./app.component";
import { DownloadComponent } from "./components/download/download.component";
import { VisualizationComponent } from "./components/visualization/visualization.component";
const appRoutes: Routes = [
    {path: "home", component: AppComponent},
    {path: "data", component: DataComponent},
    {path: "details/:mutation", component: DetailsComponent},
    {path: "download", component: DownloadComponent},
    {path: "visualization", component: VisualizationComponent},
];
export const appRoutingProviders: any[] = [];
export const routing: ModuleWithProviders<any> = RouterModule.forRoot(appRoutes);
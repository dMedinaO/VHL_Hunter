import { ModuleWithProviders } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { DetailsComponent } from './components/details/details.component';
import { DataComponent } from './components/data/data.component';
import { AppComponent } from "./app.component";

const appRoutes: Routes = [
    {path: "data", component: DataComponent},
    {path: "details/:mutation", component: DetailsComponent},
];
export const appRoutingProviders: any[] = [];
export const routing: ModuleWithProviders<any> = RouterModule.forRoot(appRoutes);
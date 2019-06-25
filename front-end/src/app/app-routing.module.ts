import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ItemListComponent } from './items/item-list/item-list.component';
import { ItemDetailComponent } from './items/components/item-detail/item-detail.component';
import { ItemFormComponent } from './items/components/item-form/item-form.component';
import { AuthComponent } from './auth/auth.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponent },
  {
    path: '',
    children: [
      { path: '', component: ItemListComponent },
      { path: ':id', component: ItemDetailComponent },
      { path: ':id/edit', component: ItemFormComponent },
      { path: ':id/create', component: ItemFormComponent }
    ],
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

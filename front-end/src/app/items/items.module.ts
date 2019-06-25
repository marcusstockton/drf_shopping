import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ItemListComponent } from './item-list/item-list.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { ItemFormComponent } from './components/item-form/item-form.component';
import { ItemDetailComponent } from './components/item-detail/item-detail.component';
import { ItemViewerComponent } from './containers/item-viewer/item-viewer.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [ItemListComponent, ItemListComponent, ItemFormComponent, ItemDetailComponent, ItemViewerComponent],
  imports: [
    CommonModule,
    RouterModule,
    NgbModule,
    FormsModule,
    ReactiveFormsModule
  ],
  exports:[
    ItemListComponent
  ]
})
export class ItemsModule { }

import { Component, OnInit } from '@angular/core';
import { ItemService } from '../item.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-item-list',
  templateUrl: './item-list.component.html',
  styleUrls: ['./item-list.component.css']
})
export class ItemListComponent implements OnInit {

  itemList: any[];

  constructor(private service: ItemService, private router: Router) {

    this.service.getItems().subscribe((result: any[]) => {
      this.itemList = result;
    }, (error) => {
      if (error.statusText) {
        console.log(error.statusText);
      } else {
        alert(error);
      }

    });

  }

  ngOnInit() {
  }

}

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ItemService } from '../../item.service';
import { Item } from '../../models/item.interface';

@Component({
  selector: 'app-item-detail',
  templateUrl: './item-detail.component.html',
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent implements OnInit {

  private itemId: number;
  private item: Item;

  constructor(private route: ActivatedRoute, private service: ItemService) { }

  ngOnInit() {
    this.itemId = parseInt(this.route.snapshot.paramMap.get('id'), 10);
    if (this.itemId) {
      this.service.getItem(this.itemId).subscribe((result) => {
        this.item = result;
      }, error => {

      });
    }
  }

  onUpdateItem(event: Item) {
    this.service.updateItem(event)
      .subscribe((data: Item) => this.item = Object.assign({}, this.item, event));
  }

}

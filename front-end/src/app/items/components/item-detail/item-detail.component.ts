import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ItemService } from '../../item.service';
import { Item } from '../../models/item.interface';
import { AuthService } from 'src/app/auth/auth.service';

@Component({
  selector: 'app-item-detail',
  templateUrl: './item-detail.component.html',
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent implements OnInit {

  private itemId: number;
  private item: Item;
  public showEditForm: boolean;

  constructor(private route: ActivatedRoute, private service: ItemService, private authService: AuthService) { }

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
      .subscribe((data: Item) => {
        this.item = Object.assign({}, this.item, event), 
        this.edit();
      }, ((error: any) => {
        console.log(error);
      }));
  }

  edit() {
    this.showEditForm = !this.showEditForm;
  }

  isLoggedIn(): boolean {
    return !this.authService.isLoggedIn();
  }

}

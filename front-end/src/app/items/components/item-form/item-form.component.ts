import { Component, OnInit, EventEmitter, Output, Input } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Item } from '../../models/item.interface';

@Component({
  selector: 'app-item-form',
  templateUrl: './item-form.component.html',
  styleUrls: ['./item-form.component.css']
})
export class ItemFormComponent implements OnInit {
  private itemForm: FormGroup;

  @Input()
  detail: Item;

  @Output()
  update: EventEmitter<Item> = new EventEmitter<Item>();

  @Output()
  create: EventEmitter<Item> = new EventEmitter<Item>();

  constructor(private fb: FormBuilder) {
    this.itemForm = this.fb.group({
      id: [''],
      title: ['', Validators.required],
      description: [''],
      price: ['']
    });
  }

  ngOnInit() {
    let item = this.detail;
    this.itemForm.setValue({id: item.id, title: item.title, description: item.description, price: item.price});
  }

  handleSubmit(item: Item, isValid: boolean) {
    if (isValid) {
      this.update.emit(item);
    }
  }
}

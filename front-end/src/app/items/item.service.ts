import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { Item } from './models/item.interface';


@Injectable({
  providedIn: 'root'
})
export class ItemService {

  private baseURL = environment.apiBaseURL + 'items';
  constructor(private httpClient: HttpClient) { }

  getItems(): Observable<Item[]> {
    return this.httpClient.get<Item[]>(`${this.baseURL}`)
      .pipe(
        tap( // Log the result or error
          // data => console.log(data),
          // error => console.log(error)
        )
      );
  }

  getItem(id: number): Observable<Item> {
    return this.httpClient.get<Item>(`${this.baseURL}/${id}`)
      .pipe(
        tap( // Log the result or error
          // data => console.log(data),
          // error => console.log(error)
        )
      );
  }

  updateItem(item: Item): Observable<Item> {
    return this.httpClient.put<Item>(`${this.baseURL}/${item.id}/`, item)
    .pipe(
      tap( // Log the result or error
        // data => console.log(data),
        // error => console.log(error)
      )
    );
  }
  removeItem(item: Item): Observable<Item> {
    return this.httpClient.delete<Item>(`${this.baseURL}/${item.id}/`)
    .pipe(
      tap( // Log the result or error
        // data => console.log(data),
        // error => console.log(error)
      )
    );
}
}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable, BehaviorSubject } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private currentUserSubject: BehaviorSubject<string>;
  private baseURL = environment.apiBaseURL + 'api-token-auth/';
  constructor(private httpClient: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<string>(localStorage.getItem('id_token'));
  }

  login(login: any): Observable<any> {
    return this.httpClient.post<any>(`${this.baseURL}`, login)
      .pipe(
        tap( // Log the result or error
           data => this.setCookie(data.token)
          // error => console.log(error)
        )
      );
  }

  public get currentUserValue(): string {
    return this.currentUserSubject.value;
  }

  isLoggedIn() {
    return this.currentUserValue !== '';
  }

  logout() {
    localStorage.removeItem('id_token');
  }

  private setCookie(token: string)  {
    localStorage.setItem('id_token', token);
  }
}

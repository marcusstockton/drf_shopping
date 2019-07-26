import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from './auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {
  private authForm: FormGroup;
  public errorList: Array<string>;

  constructor(private fb: FormBuilder, private service: AuthService, private router: Router) {
    this.authForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });

  }

  ngOnInit() {
  }

  handleSubmit(item: any, isValid: boolean) {
    if (isValid) {
      this.errorList = [];
      // Submit the form
      this.service.login(this.authForm.value).subscribe((result) => {
        this.router.navigate(['/']);
      }, (error) => {
        this.errorList.push(error.error.detail);
      });
    }
  }

}

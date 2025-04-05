import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { JobsService } from 'src/app/services/jobs.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  constructor(
    private fb: FormBuilder,
    private http: HttpClient,
    private snackBar: MatSnackBar,
    private router: Router,
    private jobService: JobsService
  ) {}

  loginForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  });

  onSubmit() {
    if (this.loginForm.invalid) {
      this.snackBar.open('Please fill in all required fields', 'Close', { duration: 3000 });
      return;
    }

    const payload = this.loginForm.value;
    // this.jobService.login(payload).subscribe((res: any) => {
    //   localStorage.setItem('access_token', res.access_token);
    //   this.snackBar.open('Login successful', 'Close', { duration: 3000 });
    //   this.router.navigate(['/job-list']); // 
    // })
    this.jobService.login(payload).subscribe({
      next: (res: any) => {
        localStorage.setItem('access_token', res.access_token);
        this.snackBar.open('✅ Login successful', 'Close', {
          duration: 3000,
          panelClass: ['mat-toolbar', 'mat-primary']
        });
        this.router.navigate(['/job-list']);
      },
      error: (err) => {
        console.log(err)
        const errorMsg = err?.error?.message || '❌ Login failed. Please try again.';
        this.snackBar.open(errorMsg, 'Close', {
          duration: 4000,
          panelClass: ['mat-toolbar', 'mat-warn']
        });
      }
    });
  }
}

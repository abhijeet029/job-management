import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})

export class JobsService {
  private apiUrl = environment.apiURL;

  constructor(private http: HttpClient) { }

  uploadResume(formData: FormData) {
    return this.http.post(`${this.apiUrl}/resume/upload`, formData);
  }

  getJobs() {
    return this.http.get(`${this.apiUrl}/jobs/list`);
  }
  login(formData: FormData ) {
    return this.http.post<any>(`${this.apiUrl}/auth/login`, formData)
  }
}

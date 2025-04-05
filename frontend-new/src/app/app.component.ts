import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Job Management';
  accessToken: any = localStorage.getItem('access_token')
  ngOnInit(){
    console.log(this.accessToken)
  }
}

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SubmittedJobsComponent } from './components/submitted-jobs/submitted-jobs.component';
import { CvUploadComponent } from './components/cv-upload/cv-upload.component';
import { LoginComponent } from './components/login/login.component';
import { AuthGuard } from './guards/auth.guard';

const routes: Routes = [
  { path: 'job-list', component: SubmittedJobsComponent, canActivate: [AuthGuard]},
  { path: 'upload-cv', component: CvUploadComponent, canActivate: [AuthGuard]},
  { path: 'login', component: LoginComponent, canActivate: [AuthGuard]}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { 

}

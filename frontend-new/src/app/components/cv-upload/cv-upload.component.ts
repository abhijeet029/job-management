import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { JobsService } from 'src/app/services/jobs.service';
import { Router } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-cv-upload',
  templateUrl: './cv-upload.component.html',
  styleUrls: ['./cv-upload.component.scss']
})
export class CvUploadComponent implements OnInit {
  jobForm: any = FormGroup;
  fileError: string | null = null;
  
  constructor(private fb: FormBuilder, 
    private jobsService: JobsService,
    private router: Router,
    private snackBar: MatSnackBar) { 
    this._initJobForm() // calling job form initialize function
  }

  // initializing job form with null
  _initJobForm = () => {
    this.jobForm = this.fb.group({
      file: [null]
    });
  }

  ngOnInit(): void {
  }

  // handling file change event
  onFileChange(event: any) {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      if (file) {
        console.log(file.type)
        const allowedTypes = ['text/csv'];
        if (allowedTypes.includes(file.type)) {
          this.fileError = null; // Reset error
          this.jobForm.patchValue({ file: file });
        } else {
          this.fileError = 'Invalid file type. Please upload a PDF, DOC, DOCX, or TXT file.';
          this.jobForm.patchValue({ file: null });
        }
      }
    }
  }

  // this function will handle upload resume functionality
  uploadResume() {
    const formData = new FormData();
    formData.append('file', this.jobForm.get('file')?.value);
    this.jobsService.uploadResume(formData).subscribe((res: any) => {
      this.snackBar.open(res?.message || 'Resume uploaded successfully', 'Close', {
        duration: 3000, // milliseconds
        horizontalPosition: 'center',
        verticalPosition: 'bottom',
        panelClass: ['custom-snackbar'] // optional for styling
      });
      setTimeout(() => {
        this.router.navigate(['/job-list']); // Replace with your desired route
      }, 2000)
    });
  }

}

import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { JobsService } from 'src/app/services/jobs.service';

export interface JobInterface {
  title: string;
  location: string;
  experience: number;
  jd: string;
  tech_skills: [string];
  salary_min: number;
  salary_max: number;
  uid: string
}

let JOB_DATA: JobInterface[] = [];

@Component({
  selector: 'app-submitted-jobs',
  templateUrl: './submitted-jobs.component.html',
  styleUrls: ['./submitted-jobs.component.scss'],
})

export class SubmittedJobsComponent implements AfterViewInit {
  displayedColumns: string[] = ['title', 'location', 'experience', 'salary', 'status', 'remarks'];
  dataSource: any = new MatTableDataSource<JobInterface>(JOB_DATA);

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  constructor(private jobsService: JobsService) { 
    this._getJobList()
  }

  ngOnInit(): void {

  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  _getJobList = () => {
    const resp = this.jobsService.getJobs().subscribe(data => {
      this.dataSource.data = data;
    })
  }

  // deleteRow(id: number) {
  //   this.dataSource.data = this.dataSource.data.filter(item => item.id !== id);
  // }

}

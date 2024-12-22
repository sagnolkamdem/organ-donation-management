import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {CommonModule} from "@angular/common";
import {MatButtonModule} from "@angular/material/button";
import {MatDialogModule, MatDialogRef} from "@angular/material/dialog";

@Component({
  selector: 'app-dialog',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatDialogModule,
    MatButtonModule
  ],
  templateUrl: './dialog.component.html',
  styleUrl: './dialog.component.scss'
})
export class DialogComponent {
  form!: FormGroup;
  submitted: boolean = false;

  constructor(public dialogRef: MatDialogRef<DialogComponent>, private formBuilder: FormBuilder) {
    this.form = this.formBuilder.group({
      donator: [null, [Validators.required]],
      organ: [null, [Validators.required]],
      availability: [1],
    })
  }

  onSubmit(): void {
    this.submitted = true;
    if (this.form.valid) {
      this.dialogRef.close(this.form.value);
    }
  }

}

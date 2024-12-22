import {Component, Inject} from '@angular/core';
import {MatButton} from "@angular/material/button";
import {MatDialogClose, MatDialogRef} from "@angular/material/dialog";
import {NgIf} from "@angular/common";
import {FormBuilder, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {MAT_DIALOG_DATA} from '@angular/material/dialog';
import {Donation} from "../../interfaces/donation";

@Component({
  selector: 'app-update-dialog',
  standalone: true,
    imports: [
        MatButton,
        MatDialogClose,
        NgIf,
        ReactiveFormsModule
    ],
  templateUrl: './update-dialog.component.html',
  styleUrl: './update-dialog.component.scss'
})
export class UpdateDialogComponent {
  form!: FormGroup;
  submitted: boolean = false;

  constructor(
    public dialogRef: MatDialogRef<UpdateDialogComponent>,
    private formBuilder: FormBuilder,
    @Inject(MAT_DIALOG_DATA) public data: Donation
  ) {
    this.form = this.formBuilder.group({
      donator: [data.donator, [Validators.required]],
      organ: [data.organ, [Validators.required]],
      availability: [data.availability],
    })
  }


  onSubmit(): void {
    this.submitted = true;
    if (this.form.valid) {
      this.dialogRef.close(this.form.value);
    }
  }
}

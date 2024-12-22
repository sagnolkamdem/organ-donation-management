import {ChangeDetectionStrategy, ChangeDetectorRef, Component, inject} from '@angular/core';
import {MatDialog, MatDialogModule} from "@angular/material/dialog";
import {MatButtonModule} from "@angular/material/button";
import {DialogComponent} from "../dialog/dialog.component";
import {CommonModule} from "@angular/common";
import {ReactiveFormsModule} from "@angular/forms";
import {DonationService} from "../../services/donation.service";
import {Donation} from "../../interfaces/donation";
import {UpdateDialogComponent} from "../update-dialog/update-dialog.component";

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatDialogModule,
    ],
  changeDetection: ChangeDetectionStrategy.OnPush,
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  readonly dialog = inject(MatDialog);
  readonly donationService: DonationService = inject(DonationService);
  donations: Donation[] = [];

  constructor(
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.getDonations();
  }

  getDonations(): void {
    this.donationService.getDonations()
      .subscribe({
        next: (data: Donation[]) => {
          this.donations = data; // Assign data to the local variable
          this.cdr.detectChanges(); // Manually trigger change detection
        },
        error: (err) => {
          console.error('Error fetching donations:', err);
        },
      });
  }

  deleteDonation(id: number): void {
    this.donationService.deleteDonation(id)
      .subscribe({
        next: (data) => {
          this.getDonations();
        },
        error: (err) => {
          console.error('Error deleting donations:', err);
        },
      });
  }

  openCreateDialog() {
    const dialogRef = this.dialog.open(DialogComponent);

    dialogRef.afterClosed().subscribe((result: Donation) => {
      if (result.donator && result.organ) {
        this.postDonations(result);
      }
    });
  }

  postDonations(data: Donation): void {
    this.donationService.postDonation(data)
      .subscribe({
        next: (message) => {
          this.getDonations();
        },
        error: (err) => {
          console.error('Error posting donations:', err);
        },
      });
  }


  openUpdateDialog(donation: Donation) {
    const dialogRef = this.dialog.open(
      UpdateDialogComponent,
      {
        data: donation
      });

    dialogRef.afterClosed().subscribe((result: Donation) => {
      if (result.donator && result.organ && donation.id) {
        this.putDonations(donation.id, result);
      }
    });
  }

  putDonations(id: number, data: Donation): void {
    this.donationService.putDonation(id, data)
      .subscribe({
        next: (message) => {
          this.getDonations();
        },
        error: (err) => {
          console.error('Error posting donations:', err);
        },
      });
  }
}

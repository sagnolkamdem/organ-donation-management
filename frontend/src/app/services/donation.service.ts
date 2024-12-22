import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { environment } from '../../environment/environment'
import {Donation} from "../interfaces/donation";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class DonationService {

  constructor(
    private http: HttpClient,
  ) { }

  getDonations(): Observable<Donation[]> {
    return this.http.get<Donation[]>(
      `${environment.apiUrl}/donations`
    );
  }

  postDonation(donation: Donation) {
    return this.http.post(
      `${environment.apiUrl}/donations`,
      donation
    );
  }

  putDonation(id: number, data: Donation){
    return this.http.put(
      `${environment.apiUrl}/donations/${id}`,
      data
    );
  }

  deleteDonation(id: number) {
    return this.http.delete(
      `${environment.apiUrl}/donations/${id}`
    );
  }
}

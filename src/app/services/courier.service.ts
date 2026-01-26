import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { environment } from '../../environments/environment';
import { Courier } from '../models/courier.model';

@Injectable({
  providedIn: 'root'
})
export class CourierService {
  private http = inject(HttpClient);
  private apiUrl = `${environment.courierApiUrl}/couriers`;

  getCouriers(): Observable<Courier[]> {
    return this.http.get<Courier[]>(this.apiUrl);
    // .pipe(tap(couriers => console.log('Fetched couriers:', couriers)));
  }
}

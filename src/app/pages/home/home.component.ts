import { Component, AfterViewInit, Inject, PLATFORM_ID, inject, OnDestroy } from '@angular/core';
import { isPlatformBrowser } from '@angular/common';
import * as L from 'leaflet';
import { CourierService } from '../../services/courier.service';
import { Courier } from '../../models/courier.model';
import { Subscription, interval, startWith, switchMap, retry } from 'rxjs';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements AfterViewInit, OnDestroy {
  private map: L.Map | undefined;
  private courierService = inject(CourierService);
  private pollingSubscription: Subscription | undefined;
  private courierLayers: L.LayerGroup = L.layerGroup();
  private courierIcon = L.icon({
    iconUrl: 'delivery.png',
    iconSize: [48, 48],
    iconAnchor: [24, 24],
    popupAnchor: [0, -48]
  });

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {}

  ngAfterViewInit(): void {
    if (isPlatformBrowser(this.platformId)) {
      this.initMap();
      this.startTracking();
    }
  }

  ngOnDestroy(): void {
    if (this.pollingSubscription) {
      this.pollingSubscription.unsubscribe();
    }
  }

  private initMap(): void {
    this.map = L.map('map').setView([-30.0346, -51.2177], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '© OpenStreetMap dependencies'
    }).addTo(this.map);

    this.courierLayers.addTo(this.map);
  }

  private startTracking(): void {
    this.pollingSubscription = interval(500)
      .pipe(
        startWith(0),
        switchMap(() => this.courierService.getCouriers()),
        retry({ delay: 3000 })
      )
      .subscribe({
        next: (couriers) => this.updateCouriersOnMap(couriers),
        error: (err) => console.error('Error fetching couriers:', err)
      });
  }

  private updateCouriersOnMap(couriers: Courier[]): void {
    if (!this.map) return;

    this.courierLayers.clearLayers();

    couriers.forEach(courier => {
      const marker = L.marker([courier.current.lat, courier.current.lon], { icon: this.courierIcon })
        .bindPopup(`Courier ID: ${courier.id}`);
      
      const line = L.polyline([
        [courier.origin.lat, courier.origin.lon],
        [courier.destiny.lat, courier.destiny.lon]
      ], {
        color: '#00bcd4',
        weight: 3,
        opacity: 0.6,
        dashArray: '5, 10'
      });

      this.courierLayers.addLayer(marker);
      this.courierLayers.addLayer(line);
    });
  }
}

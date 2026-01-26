export interface Location {
  lat: number;
  lon: number;
}

export interface Courier {
  id: number;
  origin: Location;
  destiny: Location;
  current: Location;
}

# Study Project Spec: City Courier Tracker

This specification defines the requirements for the "City Courier Tracker" application. This project is designed to mirror the architecture and technology stack of `delivery-subsidiary-frontend` to facilitate learning.

## 1. Project Overview
**Name**: City Courier Tracker
**Goal**: Build a Single Page Application (SPA) for managing delivery zones and monitoring courier status.
**Stack**: Angular 20, Angular Material, Leaflet, @ngrx/component-store, ExcelJS.

## 2. Architecture & Patterns

### 2.1 File Structure
Mimic the existing project structure:
```text
src/app/
├── components/          # Feature components
│   ├── auth/            # Login page
│   ├── dashboard/       # Main container
│   │   ├── map/         # Map visualization
│   │   └── couriers/    # Courier list/table
│   └── shared/          # Reusable UI components
├── core/
│   ├── guards/          # Auth guards
│   └── interceptors/    # HTTP interceptors
├── models/              # TypeScript Interfaces
├── services/            # Global services (Auth, etc.)
└── store/               # Global state (if needed, else ComponentStores in features)
```

### 2.2 Key Principles
*   **Standalone Components**: No NgModules.
*   **Component Store**: Use `@ngrx/component-store` for feature-level state (e.g., `CourierStore`, `ZoneStore`).
*   **Functional Interceptors**: Use `HttpInterceptorFn` (no class-based interceptors).
*   **SCSS**: Use SCSS for styling, adhering to a separate `styles/` directory for variables if needed.

## 3. Data Models

### 3.1 User
```typescript
interface User {
  id: number;
  username: string;
  role: 'ADMIN' | 'MANAGER';
  token: string;
}
```

### 3.2 Delivery Zone (GeoJSON)
```typescript
interface DeliveryZone {
  id: string;
  name: string;
  color: string;
  geometry: {
    type: 'Polygon';
    coordinates: number[][][]; // [Lat, Lng]
  };
}
```

### 3.3 Courier
```typescript
interface Courier {
  id: number;
  name: string;
  status: 'ONLINE' | 'OFFLINE' | 'BUSY';
  currentLocation?: { lat: number; lng: number };
  assignedZoneId?: string;
}
```

## 4. Feature Specifications

### Feature 1: Foundation & Layout
*   **Objective**: Setup Angular Material shell.
*   **Requirements**:
    *   Install Angular Material.
    *   Create a `DashboardComponent` with a Side Nav and Toolbar.
    *   Implement routing: `/login` (public) and `/dashboard` (protected).

### Feature 2: Authentication (Simulated)
*   **Objective**: Implement Auth flow with Interceptors.
*   **Requirements**:
    *   `AuthService`: `login(username, password)` returns an Observable of a mock User with a fake JWT.
    *   `AuthGuard`: Protect `/dashboard` routes. Redirect unauthenticated users to `/login`.
    *   `AuthInterceptor`: Attach the fake JWT to all outgoing requests (simulated by logging to console).

### Feature 3: Interactive Map (Zones)
*   **Objective**: Use Leaflet to draw zones.
*   **Requirements**:
    *   Integrate `@bluehalo/ngx-leaflet`.
    *   Display a base map (OpenStreetMap tiles).
    *   Add `leaflet-draw` controls.
    *   **Action**: Allow users to draw a polygon.
    *   **State**: When a polygon is created, save it to `ZoneStore` (local component store).
    *   **Visual**: Render saved zones on the map with different colors.

### Feature 4: Courier Management
*   **Objective**: Manage a list of items using Component Store.
*   **Requirements**:
    *   `CouriersComponent`: Display a Material Table of couriers.
    *   `CourierStore`:
        *   `state`: `{ couriers: Courier[], filter: string }`
        *   `readonly couriers$`: Selector for UI.
        *   `addCourier(courier)`: Updater to add a new row.
        *   `updateStatus(id, status)`: Effect/Updater to change status.
    *   **Interaction**: clicking a courier in the list should "pan" the map to their location (mock location).

### Feature 5: Export Data
*   **Objective**: Use non-UI libraries.
*   **Requirements**:
    *   Add an "Export Zones" button.
    *   Use `exceljs` to generate a `.xlsx` file containing Zone Name and Coordinate count.

## 5. Implementation Plan (Step-by-Step)
1.  **Init**: Create new Angular project `city-courier-tracker`.
2.  **Setup**: Configure Material, Leaflet, and Tailwind (or SCSS).
3.  **Dev**: Implement Feature 1 (Layout).
4.  **Dev**: Implement Feature 2 (Auth).
5.  **Dev**: Implement Feature 3 (Map).
6.  **Dev**: Implement Feature 4 (Couriers & Store).
7.  **Dev**: Implement Feature 5 (Excel).

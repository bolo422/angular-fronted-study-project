# Study Route: Delivery Subsidiary Frontend

This document outlines the core technologies used in the `delivery-subsidiary-frontend` project and provides a structured route to master them. The goal is to prepare you to contribute effectively to this codebase by building a smaller, focused study project.

## Core Technologies

### 1. Framework & Language
*   **Angular v20**: The latest version of the framework.
    *   *Key Concepts*: Standalone Components, Signals (likely, given the version), New Control Flow (`@if`, `@for`), Dependency Injection.
*   **TypeScript v5.9**: Strongly typed JavaScript.

### 2. State Management
*   **@ngrx/component-store**: A standalone library for managing local/component state. It's lighter than the full NgRx Store and distinct from Signals, though they can work together.

### 3. UI & Styling
*   **Angular Material**: The official component library (Tables, Dialogs, Snackbars, Inputs).
*   **SCSS**: CSS Preprocessor used for styling.
*   **Leaflet Ecosystem**:
    *   `leaflet`: Core mapping library.
    *   `@bluehalo/ngx-leaflet`: Angular wrapper for Leaflet.
    *   `leaflet-draw` & `@geoman-io/leaflet-geoman-free`: For drawing shapes (polygons) on maps.

### 4. API & Data
*   **Orval**: A tool to generate client-side models and services from OpenAPI/Swagger specs.
*   **RxJS**: Reactive programming library (Observables, Operators).
*   **ExcelJS & pdf-lib**: For generating reports/files client-side.

### 5. Quality & Tooling
*   **ESLint & Prettier**: For code linting and formatting.
*   **Jasmine & Karma**: Unit testing.
*   **Cypress**: End-to-End (E2E) testing.

---

## The Study Route

Follow this path to build up the necessary skills.

### Phase 1: Angular Modern Core
*   **Goal**: Understand the structure of an Angular 20 application without Modules (Standalone).
*   **Topics**:
    *   Standalone Components, Directives, and Pipes.
    *   The `provideHttpClient` and Interceptors (Functional Interceptors).
    *   Angular Router (Lazy loading routes).
    *   New Control Flow Syntax (`@if`, `@for`, `@switch`).
*   **Resources**: Official Angular Documentation (v18+ docs are relevant for v20 features).

### Phase 2: Reactive State & Forms
*   **Goal**: Manage data flow and user input.
*   **Topics**:
    *   **RxJS**: `map`, `switchMap`, `tap`, `catchError`, `BehaviorSubject`.
    *   **@ngrx/component-store**: Learning `readonly()`, `select()`, `updater()`, and `effect()`.
    *   **Angular Forms**: Reactive Forms, Validators, and custom Value Accessors (if needed).

### Phase 3: Maps & Visualization (The "Delivery" Domain)
*   **Goal**: Master the geospatial aspect of the project.
*   **Topics**:
    *   Setting up a Leaflet map in Angular.
    *   Adding Markers and Popups.
    *   Using `leaflet-draw` to create Polygons (Zones).
    *   Handling map events (clicks, bounds changes).

### Phase 4: API Integration & Tooling
*   **Goal**: Automate and standardize.
*   **Topics**:
    *   **Orval**: Try generating a simple service from a sample Swagger JSON.
    *   **ExcelJS**: Create a simple function to export a JSON array to an `.xlsx` file.

---

## Study Project: "City Courier Tracker"

To apply these skills, you will build **City Courier Tracker**, a simplified version of the main application.

### Concept
A dashboard for a local delivery hub manager to define delivery zones on a map and view a list of active couriers.

### Core Features to Build
1.  **Auth (Mock)**: A simple login page using `AuthService` and Interceptors.
2.  **Dashboard Layout**: A shell with a Sidebar and Header using Angular Material.
3.  **Zone Editor**: A map view where the user can draw "Delivery Zones" (Polygons) and save them to a local state.
4.  **Courier List**: A reactive table displaying dummy courier data, filtered by status (Online/Offline).
5.  **Export**: A button to download the list of Zones as an Excel file.

### Tech Stack for Study Project
*   Angular 20 (Standalone)
*   @ngrx/component-store
*   Leaflet + Leaflet Draw
*   Angular Material

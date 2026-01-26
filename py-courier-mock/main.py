import threading
import time
import math
import random
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# --- Configuration ---
NUM_COURIERS = 10
PORTO_ALEGRE_BOUNDS = {
    "lat_min": -30.25,
    "lat_max": -29.98,
    "lon_min": -51.30,
    "lon_max": -51.05
}
SPEED_DEG_PER_SEC = 0.001  # Roughly 10 meters per second (approx)
UPDATE_INTERVAL = 0.1  # Seconds

# --- Models ---

class Coordinates(BaseModel):
    lat: float
    lon: float

class CourierModel(BaseModel):
    id: int
    origin: Coordinates
    destiny: Coordinates
    current: Coordinates

# --- Logic ---

def get_random_poa_location() -> Coordinates:
    lat = random.uniform(PORTO_ALEGRE_BOUNDS["lat_min"], PORTO_ALEGRE_BOUNDS["lat_max"])
    lon = random.uniform(PORTO_ALEGRE_BOUNDS["lon_min"], PORTO_ALEGRE_BOUNDS["lon_max"])
    return Coordinates(lat=lat, lon=lon)

class Courier:
    def __init__(self, courier_id: int):
        self.id = courier_id
        start_pos = get_random_poa_location()
        self.origin = start_pos
        self.current = start_pos.model_copy()
        self.destiny = get_random_poa_location()
        
        # Calculate velocity vector
        self._update_velocity()

    def _update_velocity(self):
        dy = self.destiny.lat - self.current.lat
        dx = self.destiny.lon - self.current.lon
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance == 0:
            self.velocity_lat = 0
            self.velocity_lon = 0
        else:
            # Adjust speed by update interval to get accurate per-second speed
            step_size = SPEED_DEG_PER_SEC * UPDATE_INTERVAL
            self.velocity_lat = (dy / distance) * step_size
            self.velocity_lon = (dx / distance) * step_size

    def move(self):
        # Move
        new_lat = self.current.lat + self.velocity_lat
        new_lon = self.current.lon + self.velocity_lon
        
        # Check if reached (or passed) destiny
        step_size = SPEED_DEG_PER_SEC * UPDATE_INTERVAL
        dist_sq = (self.destiny.lat - new_lat)**2 + (self.destiny.lon - new_lon)**2
        
        if dist_sq < (step_size ** 2): # Within one step reach
            self.reach_destiny()
        else:
            self.current.lat = new_lat
            self.current.lon = new_lon

    def reach_destiny(self):
        # Current reached destiny.
        # New origin is the *current* destiny (before we pick a new one).
        self.origin = self.destiny
        # New current starts at this location (must be a copy to allow independent movement)
        self.current = self.destiny.model_copy()
        # Pick new destiny
        self.destiny = get_random_poa_location()
        self._update_velocity()

    def to_model(self) -> CourierModel:
        return CourierModel(
            id=self.id,
            origin=self.origin,
            destiny=self.destiny,
            current=self.current
        )

# --- Global State ---
couriers: List[Courier] = []

def init_couriers():
    global couriers
    couriers = [Courier(i) for i in range(1, NUM_COURIERS + 1)]

# --- Simulation Loop ---
def simulation_loop():
    while True:
        for courier in couriers:
            courier.move()
        time.sleep(UPDATE_INTERVAL)

# --- API ---
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start_simulation():
    init_couriers()
    sim_thread = threading.Thread(target=simulation_loop, daemon=True)
    sim_thread.start()

@app.get("/couriers", response_model=List[CourierModel])
def get_couriers():
    return [c.to_model() for c in couriers]

@app.get("/courier/{courier_id}", response_model=CourierModel)
def get_courier(courier_id: int):
    for c in couriers:
        if c.id == courier_id:
            return c.to_model()
    raise HTTPException(status_code=404, detail="Courier not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

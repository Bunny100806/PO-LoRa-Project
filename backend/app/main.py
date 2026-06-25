from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.simulator import run_simulation

app = FastAPI(title="PO-LoRa Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SimulationInput(BaseModel):
    devices: int
    relays: int
    traffic_load: int
    simulation_time: int
    rssi_threshold: int


@app.get("/")
def home():
    return {"message": "PO-LoRa backend is running"}


@app.post("/simulate")
def simulate(data: SimulationInput):
    return run_simulation(
        devices=data.devices,
        relays=data.relays,
        traffic_load=data.traffic_load,
        simulation_time=data.simulation_time,
        rssi_threshold=data.rssi_threshold,
    )
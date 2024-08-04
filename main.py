from enum import Enum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from models import *
from presets import p1

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Preset(int, Enum):
    one = 1
    two = 2
    three = 3


@app.get("/")
async def default():
    return {"data": p1()}

@app.get("/preset/{preset}")
async def get_preset(preset: Preset):
    if preset is Preset.one:
        return {"data": p1()}

@app.get("/preset/{preset}/export")
async def get_preset_export(preset: Preset):
    return {}

@app.post("/render")
async def render(request_model: RequestModel):
    return {"data": ResponseModel}
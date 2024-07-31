from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

from models import *

app = FastAPI()

class Preset(int, Enum):
    preset_one: 1
    preset_two: 2
    preset_three: 3


@app.get("/")
async def default():
    return get_preset(Preset.preset_one)

@app.get("/preset/{preset}")
async def get_preset(preset: Preset):
    return {"data": ResponseModel}

@app.get("/preset/{preset}/export")
async def get_preset_export(preset: Preset):
    return {}

@app.post("/render")
async def render(request_model: RequestModel):
    return {"data": ResponseModel}

@app.post("/export")
async def export(request_model: RequestModel):
    return {"data": ResponseModel}
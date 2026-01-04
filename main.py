from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.logic import evaluate_expressions
import os

app = FastAPI()

# Input model
class PlotRequest(BaseModel):
    equations: list[str]
    params: dict[str, float] = {}
    x_min: float = -10.0
    x_max: float = 10.0
    width_px: int = 800  # Used to calculate optimal point density

@app.post("/plot")
def plot(req: PlotRequest):
    # Pass the dynamic range to the logic layer
    result = evaluate_expressions(
        req.equations, 
        req.params, 
        x_min=req.x_min, 
        x_max=req.x_max,
        num_points=req.width_px  # One point per pixel for smoothness
    )
    return result

# Serve static files
# We mount the static directory to serve CSS/JS
# Use absolute path to avoid "Directory does not exist" errors
script_dir = os.path.dirname(__file__)
static_path = os.path.join(script_dir, "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(static_path, 'index.html'))

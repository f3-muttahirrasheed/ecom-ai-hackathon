from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.api import router as api_router
from backend.config import setup_cors

app = FastAPI()

# Setup CORS
setup_cors(app)

# Include API routes
app.include_router(api_router)

# Mount static frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Optional root redirect
@app.get("/")
async def root():
    return {"message": "Go to /frontend/index.html for the UI"}

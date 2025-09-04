from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.routers import research

app = FastAPI(title="Compliance Research Assistant - API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)

app.include_router(research.router, prefix="/v1")

@app.get("/health")
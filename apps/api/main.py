from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.api.routers import research

app = FastAPI(title="Compliance Research Assistant - API", version="0.1.0")

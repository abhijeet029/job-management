from fastapi import FastAPI
from app.api.routes import jobs, resume
from app.core.database import Base, engine
from app.core.minioclient import create_minio_bucket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:4200",  # React/Vue/Angular dev server
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)
# Create database tables
Base.metadata.create_all(bind=engine)

# Ensure MinIO bucket exists
# Register routes
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(resume.router, prefix="/resume", tags=["Resume"])

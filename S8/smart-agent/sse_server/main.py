from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_server.routes import gmail, drive

app = FastAPI()

# Allow CORS for all origins (optional: restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gmail.router)
app.include_router(drive.router)


@app.get("/")
def root():
    return {"message": "SSE server running"}

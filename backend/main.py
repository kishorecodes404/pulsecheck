from fastapi import FastAPI
import requests
import time
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "PulseCheck API is running"}


@app.get("/check")
def check_url(url: str):
    start_time = time.time()

    try:
        response = requests.get(url, timeout=10)
        response_time = round((time.time() - start_time) * 1000)

        return {
            "url": url,
            "status": "Online",
            "status_code": response.status_code,
            "response_time_ms": response_time
        }

    except requests.RequestException:
        return {
            "url": url,
            "status": "Offline",
            "status_code": None,
            "response_time_ms": None
        }
# main.py
from fastapi import FastAPI
from config import settings

app = FastAPI(debug=settings.debug)

@app.get("/test")
def root():
    return {"the app is running"}
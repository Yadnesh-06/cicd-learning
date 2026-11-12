"""Defines a small FastAPI application for CI/CD training."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD Demo Application"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a-b}


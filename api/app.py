from fastapi import FastAPI, HTTPExeception

app = FastAPI()

@app.get("/api")
def index():
    return {"message": "Welcome to Health API"}
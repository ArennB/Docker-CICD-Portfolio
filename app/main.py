from fastapi import FastAPI

app = FastAPI()

# Used as a basic confirmation that the API is online
@app.get("/")
def home():
    return {"message": "API is running"}

# Used by cloud enviornments to ensure app is working
@app.get("/health")
def health():
    return{"status": "healthy"}

# Track application versions
@app.get("/version")
def version():
    return{"version": "1.0.0"}
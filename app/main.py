from fastapi import FastAPI

app = FastAPI(title="NexusWorkplace")

@app.get("/")
def home():
    return {"status": "NexusWorkplace online", "versao": "0.1.0"}
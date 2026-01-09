from fastapi import FastAPI

app = FastAPI(
    title="MED-ORDER-CHECK",
    version="0.1.0",
    description="Medical order validation service"
)

@app.get("/")
def healthcheck():
    return {"status": "ok"}

from fastapi import FastAPI
from .models import OrderCheckRequest, OrderCheckResponse, Issue
from .engine import run_checks

app = FastAPI(
    title="MED-ORDER-CHECK",
    version="0.1.0",
    description="Clinical order validation service"
)

@app.post("/check-order", response_model=OrderCheckResponse)
def check_order(order: OrderCheckRequest):
    raw_issues, severity = run_checks(order)
    issues = [Issue(**i) for i in raw_issues]
    return OrderCheckResponse(issues=issues, severity=severity)

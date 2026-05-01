from fastapi import FastAPI
from app.schemas import OrderRequest
from app.ai import parse_order
import json

app = FastAPI()

@app.post("/parse-order")
def parse(req: OrderRequest):
    ai_result = parse_order(req.text)

    try:
        data = json.loads(ai_result)
        return data
    except:
        return {"error": "AI response invalid", "raw": ai_result}
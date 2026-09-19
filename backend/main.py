from fastapi import FastAPI, Request
import json
from pathlib import Path

app = FastAPI()

# Load orders from the JSON file next to this script
ORDERS_FILE = Path(__file__).parent / "orders.json"


def load_orders():
    with open(ORDERS_FILE, "r") as file:
        return json.load(file)


@app.get("/")
def health_check():
    return {"message": "BurgerBot backend is running"}


@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    # Dialogflow ES sends a JSON body with queryResult
    body = await request.json()

    # Get parameters safely so missing fields do not crash the app
    query_result = body.get("queryResult", {})
    parameters = query_result.get("parameters", {})
    order_number = parameters.get("order_number")

    # Dialogflow may send numbers; convert to string for lookup
    if order_number is not None:
        order_number = str(int(order_number)).strip() 

    if not order_number:
        text = "Sorry, I need an order number to check the status."
        return {"fulfillmentText": text}

    orders = load_orders()
    order = orders.get(order_number)

    if order:
        text = f"Order {order_number} is {order['status']}."
    else:
        text = f"Sorry, I couldn't find order {order_number}."

    # Simple Dialogflow ES fulfillment response
    return {"fulfillmentText": text}


# Used when running `python main.py`; Cloud Run uses the Procfile instead
if __name__ == "__main__":
    import os
    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

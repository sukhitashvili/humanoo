import logging
import os

import uvicorn
from fastapi import FastAPI

from model import Model, Input

logger = logging.getLogger(__name__)

model = Model()
app = FastAPI(title="Blueprint Generator", version="0.1.0")


@app.get("/")
def read_root():
    """Root url"""
    return 'API is working use "/docs" route to use different implemented routes'


@app.post(
    "/query",
    summary="Preferred product",
    description="Returns preferred product",
)
async def query(
        request: Input,
):
    try:
        prediction = model.predict(input_data=request)
        response = dict()
        response['status'] = 'success'
        response['message'] = prediction
        return response

    except Exception as exception:
        response = dict()
        response['error'] = f"An error occurred: {exception}"
        response['status'] = 'failed'
    return response


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")  # Default to localhost if not set
    port = int(os.getenv("PORT", 8000))  # Default port 8000 if not set
    uvicorn.run(app, host=host, port=port)

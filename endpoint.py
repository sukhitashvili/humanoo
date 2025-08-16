import logging

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from model import Model, Input

logger = logging.getLogger(__name__)

model = Model()
app = FastAPI(title="Recommender", version="0.1.0")


@app.get("/")
def read_root():
    """Root url"""
    return 'API is working use "/docs" route to use different implemented routes'


class Response(BaseModel):
    topic_name: str


@app.post("/query",summary="Preferred product", description="Returns preferred product", response_model=Response)
async def query(request: Input):
    try:
        prediction = model.predict(input_data=request)
        return JSONResponse(
            status_code=200,
            content={
                "topic_name": prediction,
            }
        )

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": f"HTTPException error: {e.detail}"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Exception error: {str(e)}"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

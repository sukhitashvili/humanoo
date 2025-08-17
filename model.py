import pickle as pkl

import numpy as np
from pydantic import BaseModel, Field


class Input(BaseModel):
    age: int = Field(
        gt=0,
        le=120,
        description="The age of the person in years. Must be between 1 and 120."
    )
    workouts_per_week: int = Field(
        ge=0,
        le=7,
        description="The number of times the person works out per week. Must be between 0 and 7."
    )


class Model:
    def __init__(self):
        with open("scaler.pkl", "rb") as f:
            scaler = pkl.load(f)
        with open("kmeans.pkl", "rb") as f:
            kmeans = pkl.load(f)
        self.scaler = scaler
        self.kmeans = kmeans
        self.index_to_product = {1: 'Recipes', 2: 'body workout', 0: 'productivity'}

    def predict(self, input_data: Input):
        array = np.array([input_data.age, input_data.workouts_per_week]).reshape((1, -1))
        scaled_data = self.scaler.transform(array)
        cluster_labels = self.kmeans.predict(scaled_data).item()
        return self.index_to_product[cluster_labels]

if __name__ == "__main__":
    m = Model()
    d = Input(age=20, workouts_per_week=5)
    print(m.predict(input_data=d))

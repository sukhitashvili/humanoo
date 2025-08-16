## Introduction

My solution for the case study is explained in - [case_study.pdf](./case_study.pdf) file, 
which I recommend to read first before going over the code.

## 📦 Requirements
Python 3.12+

## 📂 Project Structure

- [endpoint.py](./endpoint.py) - FastAPI app.
- [model.py](./model.py) - The clustering model code file.
- [Dockerfile](./Dockerfile) - The docker file.
- [data_clustering.ipynb](./data_clustering.ipynb) - Contains code used to create clustering model.
- [data.csv](./data.csv) - The toy data.
- [kmeans.pkl](./kmeans.pkl) - stored clustering model file.
- [scaler.pkl](./scaler.pkl) - stored clustering model file stats.

## 📌 Endpoints

`POST /process` - Processes an application object and returns extracted features.
### Request Body:
```JSON
{
  "age": int,
  "workouts_per_week": int
}
```
### Response:
```JSON
{
  "topic_name": string,
}
```

## ▶️ Commands to Build, Run, and Test the App Locally

Start the application locally:
```bash
pip install -r requirements.txt
uvicorn endpoint:app --host 0.0.0.0 --port 8000
```

Or Start the application using **Docker**, steps:

✅ Step 1: Build the Docker image
```bash
docker build -t my-fastapi-app .
```
✅ Step 2: Run the container
```bash
docker run -d -p 8000:8000 --name fastapi-test my-fastapi-app
```

## 🛠️ Test it
In your browser, go to: `http://localhost:8000/docs`




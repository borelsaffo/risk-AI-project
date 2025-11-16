# Risk AI Project - Dockerized demo

This project is a minimal Dockerized example to deploy an AI-based **risk scoring** service.
It contains:
- `api/` : FastAPI application exposing a `/scoring` endpoint that loads a trained model
- `worker/` : simple worker that simulates asset events and calls the API
- `docker-compose.yml` : to run everything locally

## How to run
```bash
cd risk_ai_project
docker-compose up --build
```

Then explore the API docs at: http://localhost:8000/docs

## Files
- `api/risk_model.joblib` : a simple logistic regression trained on synthetic data (for demo)
- `api/main.py` : FastAPI application
- `worker/worker.py` : simple worker sending requests
- `docker-compose.yml` : compose file

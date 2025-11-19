# Simulation Job Queue API

## Project Title & Description
REST API that mimics a high-throughput simulation job manager for R&D teams. It models how engineers submit, track, and inspect computational experiments in a lightweight queue without external dependencies.

## Tech Stack
- Python 3.10
- FastAPI
- Docker
- Docker Compose
- Pydantic

## Features
- Job creation with auto-generated UUIDs
- Status tracking across `PENDING`, `RUNNING`, `COMPLETED`, `FAILED`
- Docker containerization for one-command setup
- Automatic interactive documentation via Swagger UI

## How to Run
```bash
docker-compose up --build
```
Once the services finish building, open `http://localhost:8000/docs` for interactive API testing.

## API Endpoints
- `POST /jobs` — Create a new simulation job (default status `PENDING`).
- `GET /jobs/{job_id}` — Retrieve details for a specific job.
- `GET /jobs` — List all jobs currently in the in-memory store.

## Future Improvements
For production use, this service would integrate PostgreSQL for durable storage and an asynchronous worker (e.g., Celery) to execute real simulation workloads off the main request thread.



# Simulation Job Queue API

A containerised REST API that simulates a high-throughput job queue for computational workloads. Built with FastAPI and Docker, with full observability via Prometheus and Grafana.

## Tech Stack

- **Python 3.10** — application logic
- **FastAPI** — REST API framework with auto-generated Swagger docs
- **Pydantic** — data validation and serialisation
- **Docker + Docker Compose** — containerisation and multi-service orchestration
- **Prometheus** — metrics scraping
- **Grafana** — metrics visualisation
- **pytest** — automated testing
- **GitHub Actions** — CI pipeline

## Features

- Job submission with auto-generated UUIDs
- Automatic job lifecycle management via background tasks — jobs transition through `PENDING → RUNNING → COMPLETED`
- Real-time observability via `/metrics` endpoint
- Health check endpoint at `/health`
- Interactive API docs at `/docs`
- Automated tests and Docker build checks on every push

## How to Run

```bash
docker-compose up --build
```

| Service | URL |
|---------|-----|
| API | http://localhost:8000 |
| Swagger Docs | http://localhost:8000/docs |
| Metrics | http://localhost:8000/metrics |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs` | Submit a new simulation job |
| GET | `/jobs` | List all jobs |
| GET | `/jobs/{job_id}` | Get a specific job by ID |
| GET | `/health` | Service health check |
| GET | `/metrics` | Prometheus metrics |

## Project Structure

    ├── app/
    │   ├── main.py           — FastAPI app entry point
    │   ├── models.py         — Internal data models
    │   ├── routers/
    │   │   └── jobs.py       — Job endpoint logic and background tasks
    │   └── schemas/
    │       └── jobs.py       — Request and response schemas
    ├── monitoring/
    │   └── prometheus/
    │       └── prometheus.yml — Prometheus scrape config
    ├── tests/
    │   └── test_jobs.py      — API tests
    ├── .github/
    │   └── workflows/
    │       └── ci.yml        — GitHub Actions CI pipeline
    ├── Dockerfile
    ├── docker-compose.yml
    └── requirements.txt

## Observability

Prometheus scrapes the `/metrics` endpoint every 15 seconds. Grafana visualises the metrics on port 3000. Default Grafana login is `admin/admin`.

## Future Improvements

- PostgreSQL for persistent job storage
- Celery for real background job execution
- JWT authentication
- Grafana dashboard as code


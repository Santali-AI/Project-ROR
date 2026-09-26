# ROR — Resonance • Observation • Relationship

ROR is a research-safe, local-first MVP for studying multispecies communication patterns. It records observations, analyzes uploaded audio into acoustic features and provisional signal segments, captures evidence-based hypotheses, and logs experimental responses.

> **Scientific boundary:** ROR never presents a hypothesis as a verified translation. Every output is labelled **OBSERVED**, **LIKELY**, **POSSIBLE**, or **UNKNOWN** and tied to recorded evidence.

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Open [http://localhost:3000](http://localhost:3000). The API docs are at [http://localhost:8000/docs](http://localhost:8000/docs).

For local development:

```bash
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

cd frontend && npm install && npm run dev
```

## MVP capabilities

- Five initial species: cow, cat, dog, bird, and elephant.
- Responsive research dashboard with species selection, live/demo waveform, signal timeline, evidence dashboard, and an experiment composer.
- Audio upload endpoint that produces deterministic demo-safe acoustic features and segments (swap in a DSP/ML pipeline later).
- PostgreSQL-ready SQLAlchemy models, SQLite local fallback, seed observations, structured experiment records, and statistics.
- Explicit playback safety constraints; generated signals are experimental parameter suggestions only.

## API

- `POST /api/observations`
- `POST /api/audio/analyze`
- `GET /api/observations/{id}`
- `POST /api/interpretations`
- `POST /api/experiments`
- `GET /api/species`
- `GET /api/signals/{id}`
- `GET /api/research/statistics`

See [architecture documentation](docs/architecture.md) for design and data flow.

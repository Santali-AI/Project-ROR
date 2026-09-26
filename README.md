# ROR — Resonance • Observation • Relationship

AI multispecies communication research & interaction platform. ROR analyzes animal audio/video/context and records hypotheses without presenting them as verified translations.

## Evidence contract
Every interpretation is exactly one of `OBSERVED`, `LIKELY`, `POSSIBLE`, `UNKNOWN`. Confidence is evidence-weighted, not a claim of semantic certainty. A response experiment is always labeled experimental.

## MVP
- Species selector: cow, cat, dog, birds, elephant
- Audio upload + waveform/spectrogram
- Signal segmentation + acoustic feature extraction
- Demo clustering / similarity analysis
- PostgreSQL observation, signal, interpretation and experiment records
- Research-safe interpretation dashboard
- Human response + experimental signal generator
- Experiment response logging
- Docker Compose
- API tests

## Run
1. Copy `.env.example` to `.env`.
2. `docker compose up --build`
3. Frontend: http://localhost:3000
4. API docs: http://localhost:8000/docs

For a no-Docker backend, create a Python 3.11+ environment and run `pip install -r backend/requirements.txt`, then `uvicorn app.main:app --reload --app-dir backend`.

The current analyzer is deliberately a deterministic demo/feature pipeline. It does not claim semantic translation. Real trained models/datasets can be plugged into `backend/app/services/analyzer.py` later.

## Structure
```
frontend/  Next.js + TypeScript + Tailwind
backend/   FastAPI + SQLAlchemy + scientific feature pipeline
 db/       PostgreSQL initialization
 docs/     architecture and research protocol
```

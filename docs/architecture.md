# ROR architecture

## Flow
`Animal → capture/upload → acoustic segmentation → pattern/context evidence → research hypothesis → human-reviewed experimental response → response monitoring → reproducible dataset`

The frontend is a Next.js dashboard. The FastAPI service validates and persists structured records. SQLAlchemy uses PostgreSQL in Docker and can use SQLite in local testing. Audio analysis is intentionally an adapter: the MVP derives non-semantic, deterministic placeholder features from file metadata. This is **not** a translation model.

## Safety model

`EvidenceLevel` is required on interpretations. A hypothesis is kept separate from observed features and from a human message. Experimental playback is hard-capped at 70 dB SPL and marked `EXPERIMENTAL — NOT VERIFIED LANGUAGE`. Every experiment stores generated parameters, the response, and notes so later models can use positive, negative, and uncertain outcomes rather than a single user's label.

## Future pipeline boundary

Replace `app/services/analysis.py` with: noise reduction → segmentation → spectrogram → acoustic features → embedding → clustering/anomaly detection. Video and context embeddings join the acoustic embedding only after validation across individuals and environments.

import logging
from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, select
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Animal, Experiment, Interpretation, Observation, Signal
from .schemas import ExperimentCreate, InterpretationCreate, ObservationCreate
from .services import analyze_upload
logging.basicConfig(level=logging.INFO)
app = FastAPI(title="ROR Research API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])

SPECIES = [{"id":"cow","label":"Cow","icon":"🐄"},{"id":"cat","label":"Cat","icon":"🐈"},{"id":"dog","label":"Dog","icon":"🐕"},{"id":"bird","label":"Birds","icon":"🦜"},{"id":"elephant","label":"Elephant","icon":"🐘"}]
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    with Session(engine) as db:
        if not db.scalar(select(Animal.id).limit(1)):
            db.add_all([Animal(species="elephant", name="Nia", location="Savannah enclosure"), Animal(species="dog", name="Milo", location="Field study")]); db.commit()
@app.get("/health")
def health(): return {"status":"ok"}
@app.get("/api/species")
def species(): return SPECIES
@app.post("/api/observations", status_code=201)
def create_observation(payload: ObservationCreate, db: Session = Depends(get_db)):
    if not db.get(Animal, payload.animal_id): raise HTTPException(404, "Animal not found")
    value=Observation(**payload.model_dump()); db.add(value); db.commit(); db.refresh(value); return value
@app.get("/api/observations/{observation_id}")
def observation(observation_id: int, db: Session = Depends(get_db)):
    value=db.get(Observation, observation_id)
    if not value: raise HTTPException(404, "Observation not found")
    return value
@app.post("/api/audio/analyze")
def audio_analyze(file: UploadFile = File(...)):
    if not (file.content_type or "").startswith("audio/"): raise HTTPException(415, "Upload an audio file")
    return analyze_upload(file)
@app.post("/api/interpretations", status_code=201)
def create_interpretation(payload: InterpretationCreate, db: Session = Depends(get_db)):
    if not db.get(Signal, payload.signal_id): raise HTTPException(404, "Signal not found")
    value=Interpretation(**payload.model_dump()); db.add(value); db.commit(); db.refresh(value); return value
@app.get("/api/signals/{signal_id}")
def signal(signal_id: int, db: Session = Depends(get_db)):
    value=db.get(Signal, signal_id)
    if not value: raise HTTPException(404, "Signal not found")
    return value
@app.post("/api/experiments", status_code=201)
def create_experiment(payload: ExperimentCreate, db: Session = Depends(get_db)):
    if not db.get(Interpretation, payload.interpretation_id): raise HTTPException(404, "Interpretation not found")
    signal={"frequency_hz":payload.frequency_hz,"duration_seconds":payload.duration_seconds,"repetition":payload.repetition}
    value=Experiment(interpretation_id=payload.interpretation_id,human_message=payload.human_message,generated_signal=signal,playback_metadata={"db_spl":payload.playback_db_spl,"status":"EXPERIMENTAL — NOT VERIFIED LANGUAGE"},researcher_notes=payload.researcher_notes)
    db.add(value); db.commit(); db.refresh(value); return value
@app.get("/api/research/statistics")
def statistics(db: Session = Depends(get_db)):
    return {"observations":db.scalar(select(func.count(Observation.id))) or 0,"signals":db.scalar(select(func.count(Signal.id))) or 0,"experiments":db.scalar(select(func.count(Experiment.id))) or 0,"verified_translations":0,"safety":"All interpretations remain evidence-labelled research hypotheses."}

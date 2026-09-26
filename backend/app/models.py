from datetime import datetime
from sqlalchemy import JSON, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Animal(Base):
    __tablename__ = "animals"
    id: Mapped[int] = mapped_column(primary_key=True)
    species: Mapped[str] = mapped_column(String(40), index=True)
    name: Mapped[str] = mapped_column(String(80))
    location: Mapped[str] = mapped_column(String(120))
    age: Mapped[str | None] = mapped_column(String(30), nullable=True)
    sex: Mapped[str | None] = mapped_column(String(20), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

class Observation(Base):
    __tablename__ = "observations"
    id: Mapped[int] = mapped_column(primary_key=True)
    animal_id: Mapped[int] = mapped_column(ForeignKey("animals.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    audio_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    video_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    environmental_context: Mapped[str] = mapped_column(Text, default="")
    behaviour: Mapped[str] = mapped_column(Text, default="")

class Signal(Base):
    __tablename__ = "signals"
    id: Mapped[int] = mapped_column(primary_key=True)
    observation_id: Mapped[int] = mapped_column(ForeignKey("observations.id"))
    frequency_features: Mapped[dict] = mapped_column(JSON)
    duration: Mapped[float] = mapped_column(Float)
    repetition: Mapped[int] = mapped_column(Integer)
    classification: Mapped[str] = mapped_column(String(80))
    confidence: Mapped[float] = mapped_column(Float)

class Interpretation(Base):
    __tablename__ = "interpretations"
    id: Mapped[int] = mapped_column(primary_key=True)
    signal_id: Mapped[int] = mapped_column(ForeignKey("signals.id"))
    hypothesis: Mapped[str] = mapped_column(Text)
    evidence_count: Mapped[int] = mapped_column(Integer)
    confidence: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(30))

class Experiment(Base):
    __tablename__ = "experiments"
    id: Mapped[int] = mapped_column(primary_key=True)
    interpretation_id: Mapped[int] = mapped_column(ForeignKey("interpretations.id"))
    human_message: Mapped[str] = mapped_column(Text)
    generated_signal: Mapped[dict] = mapped_column(JSON)
    playback_metadata: Mapped[dict] = mapped_column(JSON)
    animal_response: Mapped[str | None] = mapped_column(Text, nullable=True)
    result: Mapped[str] = mapped_column(String(30), default="pending")
    researcher_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

from pydantic import BaseModel, Field
from typing import Literal

EvidenceLevel = Literal["OBSERVED", "LIKELY", "POSSIBLE", "UNKNOWN"]
class ObservationCreate(BaseModel):
    animal_id: int
    environmental_context: str = Field(max_length=2000)
    behaviour: str = Field(max_length=2000)
    audio_url: str | None = None
    video_url: str | None = None
class InterpretationCreate(BaseModel):
    signal_id: int
    hypothesis: str = Field(min_length=3, max_length=2000)
    evidence_count: int = Field(ge=0)
    confidence: float = Field(ge=0, le=100)
    status: EvidenceLevel
class ExperimentCreate(BaseModel):
    interpretation_id: int
    human_message: str = Field(min_length=1, max_length=500)
    frequency_hz: int = Field(ge=20, le=30000)
    duration_seconds: float = Field(gt=0, le=30)
    repetition: int = Field(ge=1, le=10)
    playback_db_spl: int = Field(ge=20, le=70)
    researcher_notes: str | None = Field(default=None, max_length=2000)

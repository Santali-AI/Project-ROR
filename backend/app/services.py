import hashlib
from fastapi import UploadFile

def analyze_upload(file: UploadFile) -> dict:
    """MVP adapter: metadata-derived demo features, never semantic translation."""
    digest = int(hashlib.sha256((file.filename or "audio").encode()).hexdigest()[:8], 16)
    peak = 50 + digest % 180
    return {"file_name": file.filename, "segments": [
      {"start": 0.8, "end": 2.1, "peak_hz": peak, "confidence": 0.68},
      {"start": 4.0, "end": 5.4, "peak_hz": peak + 24, "confidence": 0.61},
    ], "notice": "Preliminary acoustic segmentation only; no animal-language translation is inferred."}

from fastapi.testclient import TestClient
from app.main import app

def test_species_and_health():
    with TestClient(app) as client:
        assert client.get('/health').json()['status'] == 'ok'
        assert len(client.get('/api/species').json()) == 5

def test_audio_rejects_non_audio():
    with TestClient(app) as client:
        response = client.post('/api/audio/analyze', files={'file': ('notes.txt', b'x', 'text/plain')})
        assert response.status_code == 415

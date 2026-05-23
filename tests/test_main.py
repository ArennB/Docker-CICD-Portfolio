from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Sends fake GET request to "/", equivalent of visiting http://localhost:8000/
# Verifies that the endpoint works, server is responding correctly, and data return is correct
def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200 #assertations verify expected behavion (i.e 200 OK)
    assert response.json() == {"message": "API is running"} # Convert API respnse into python dict confirming correct response

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_version_endpoint():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}
    
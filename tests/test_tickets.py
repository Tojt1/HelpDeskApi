import pytest
from fastapi.testclient import TestClient
from main import app

class Test_tickets:
    client = TestClient(app)
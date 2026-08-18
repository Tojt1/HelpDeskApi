from fastapi.testclient import TestClient
from main import app
from backend.users.service import decode_token

class Test_tickets:
    client = TestClient(app)
    app.dependency_overrides[decode_token] = lambda: 1

    def test_create_ticket(self):
        response = self.client.post("/tickets", json={
            "title":"pytest",
            "description":"test",
            "priority":1,
            "category":"test"
        })

        assert response.status_code == 200

    def test_get_tickets(self):
        response = self.client.get("/tickets")

        assert response.status_code == 200

    def test_get_ticket_by_id(self):
        response = self.client.get("/tickets/5")

        assert response.status_code == 200


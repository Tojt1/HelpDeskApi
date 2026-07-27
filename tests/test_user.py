from  fastapi.testclient import TestClient
from main import app

class TestUsers:
    client = TestClient(app)

    def test_get_users(self):
        response = self.client.get("/")

        assert response.status_code == 200

    def test_create_user(self):
        response = self.client.post("/add-user", json={
            "name": "Pytest",
            "email": "pytest@gmail.com",
            "password": "test123"
        })

        assert response.status_code == 200

    def test_login_user(self):
        response = self.client.post("login", json={
            "email":"test@gmail.com",
            "password":"test123!"
        })

        assert response.status_code == 200

    def test_return_account_inf(self):
        response = self.client.get("/me?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OH0.3LGO4S-wfU3t-3XNfUWoN7a8b5UZr0ER_2pPkXioYzA")

        assert response.status_code == 200


from fastapi.testclient import TestClient
from main import app
from backend.users.service import decode_token

class Test_Comments:
    client = TestClient(app)
    app.dependency_overrides[decode_token["id"]] = lambda:8

    def test_get_all_coemments(self):
        response = self.client.get("/tickets/4/comments")

        assert response.status_code == 200

    def test_create_comment(self):
        response = self.client.post("/tickets/4/comments", json={
            "content":"test"
        })

        assert response.status_code == 200

    def test_get_comment_by_id(self):
        response = self.client.get("tickets/4/comments/2")

        assert response.status_code == 200

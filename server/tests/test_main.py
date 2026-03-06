def test_root_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200
def test_user_login(client):
    register_response = client.post(
        "/register",
        json={
            "name": "vichu",
            "email": "vichu@example.com",
            "password": "student123"
        }
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/login",
        json={
            "email": "vichu@example.com",
            "password": "student123"
        }
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_task(client):

    client.post(
        "/register",
        json={
            "name": "taskmanager",
            "email": "vichu@example.com",
            "password": "student123"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "email": "vichu@example.com",
            "password": "student123"
        }
    )

    token = login_response.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }


    task_response = client.post(
        "/tasks",
        json={
            "title": "Complete Python assignment",
            "description": "Finish FastAPI project",
            "status": "pending"
        },
        headers=headers
    )


    assert task_response.status_code == 201

    task_data = task_response.json()

    assert task_data["title"] == "Complete Python assignment"
    assert task_data["status"] == "pending"

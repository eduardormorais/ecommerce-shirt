import json


def test_create_user_valid_dict(flask_app, user_faker_dict):
    resp = flask_app.post(
        "/api/user", json=user_faker_dict, headers={"Content-Type": "application/json"}
    )
    assert resp.status_code == 201
    result = resp.get_json()
    assert result.get("user").get("id")

def test_create_user_invalid_dict(flask_app, user_invalid_faker_dict):
    resp = flask_app.post(
        "/api/user", json=user_invalid_faker_dict, headers={"Content-Type": "application/json"}
    )
    assert resp.status_code == 400


def test_get_all_users(flask_app):
    resp = flask_app.get("/api/user")
    assert resp.status_code == 200


def test_get_one_user(flask_app, user_faker_dict):
    resp = flask_app.get(
        f"/api/user/1", headers={"Content-Type": "application/json"}
    )
    assert resp.status_code == 200
    user_result = json.loads(resp.data)
    assert user_result.get("email")
    assert user_result.get("fullname")

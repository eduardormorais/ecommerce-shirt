def test_get_all_users(flask_app):
    resp = flask_app.get("/api/user")
    assert resp.status_code == 200


def test_create_user(flask_app, user_faker_dict):
    resp = flask_app.post(
        "/api/user", json=user_faker_dict, headers={"Content-Type": "application/json"}
    )
    assert resp.status_code == 200

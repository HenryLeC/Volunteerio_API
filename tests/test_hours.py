import json

import pytest
from API import app
from DbSetup import makeDB
from flask.testing import FlaskClient

adm_acc_token = ""
stu_acc_token = ""

hours_id = ""


@pytest.fixture(scope="module", autouse=True)
def set_up():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../test.db"
    app.config['TESTING'] = True

    makeDB()


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../test.db"
    app.config['TESTING'] = True

    yield app.test_client()


def test_login(client: FlaskClient):
    # Admin
    login = client.post('/api/login', data=dict(
        username="U2",
        password="12345"
    ), follow_redirects=True)

    global adm_acc_token
    adm_acc_token = json.loads(login.data)["key"]

    assert b'admin' in login.data

    # Student
    login = client.post('/api/login', data=dict(
        username="U1",
        password="12345"
    ), follow_redirects=True)

    global stu_acc_token
    stu_acc_token = json.loads(login.data)["key"]

    assert b'student' in login.data


def test_add_hours(client: FlaskClient):
    add_hours = client.post("/api/addhours", data={
        "x-access-token": stu_acc_token,
        "hours": 5,
        "reason": "TEST REASON",
        "desc": "TEST DESCRIPTION"
    })

    assert b"Hours added" in add_hours.data


def test_view_notifs(client: FlaskClient):
    notifs = client.post("/api/Notifications", data={
        "x-access-token": adm_acc_token
    })

    assert b"requested new hours." in notifs.data

    notifs = json.loads(notifs.data)
    global hours_id
    hours_id = notifs[0]["ID"]


def test_view_student(client: FlaskClient):
    student = client.post("/api/StudentHours", data={
        "x-access-token": adm_acc_token,
        "id": hours_id
    })

    assert b"TEST REASON" in student.data

import json
from datetime import datetime

import pytest
from API import app
from DbSetup import makeDB
from flask.testing import FlaskClient

adm_acc_token = ""
com_acc_token = ""
stu_acc_token = ""


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

    # Community
    login = client.post('/api/login', data=dict(
        username="U3",
        password="12345"
    ), follow_redirects=True)

    global com_acc_token
    com_acc_token = json.loads(login.data)["key"]

    assert b'community' in login.data

    # Student
    login = client.post('/api/login', data=dict(
        username="U1",
        password="12345"
    ), follow_redirects=True)

    global stu_acc_token
    stu_acc_token = json.loads(login.data)["key"]

    assert b'student' in login.data


def test_add_opp(client: FlaskClient):
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S") + "-05:00"
    add_opp = client.post('/api/AddOpp', data={
        "x-access-token": adm_acc_token,
        "Name": "Test Opp",
        "Date": now,
        "Location": "Test Location",
        "Hours": 5,
        "Class": "Test Class",
        "MaxVols": 30,
        "Description": "Desc"
    })

    assert b"Opportunity Added" in add_opp.data


def test_sign_in_students(client: FlaskClient):
    sign_in = client.post('/api/SignInStudents', data={
        "x-access-token": adm_acc_token,
        "OppId": 1
    })

    assert sign_in.status_code == 200


def test_my_opps(client: FlaskClient):
    my_opps = client.post('/api/MyOpps', data={
        "x-access-token": adm_acc_token
    })

    assert my_opps.status_code == 200


def test_booked_students(client: FlaskClient):
    booked_students = client.post('/api/BookedStudents', data={
        "x-access-token": adm_acc_token,
        "OppId": 1
    })

    assert booked_students.status_code == 200

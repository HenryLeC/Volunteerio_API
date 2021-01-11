import json
from datetime import datetime, timedelta

import pytest
from API import app
from DbSetup import makeDB
from flask.testing import FlaskClient

adm_acc_token = ""
com_acc_token = ""
stu_acc_token = ""

adm_clock_code = ""
com_clock_code = ""

adm_msg_id = ""
com_msg_id = ""


@pytest.fixture(scope="module", autouse=True)
def set_up():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
    app.config['TESTING'] = True

    makeDB()


@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
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
    # Admin
    now = (datetime.utcnow() + timedelta(hours=1)
           ).strftime("%Y-%m-%dT%H:%M:%S") + "-05:00"
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

    # Community
    add_opp = client.post('/api/AddOpp', data={
        "x-access-token": com_acc_token,
        "Name": "Test Opp",
        "Date": now,
        "Location": "Test Location",
        "Hours": 5,
        "Class": "Test Class",
        "MaxVols": 30,
        "Description": "Desc"
    })

    assert b"Opportunity Added" in add_opp.data


def test_list_uncof_opps(client: FlaskClient):
    unconf_opps = client.post("/api/UnconfOpps", data={
        "x-access-token": adm_acc_token
    })

    assert b"2" in unconf_opps.data


def test_confirm_opp(client: FlaskClient):
    conf_opp = client.post("/api/ConfDelOpp", data={
        "x-access-token": adm_acc_token,
        "Mode": "Confirm",
        "ID": 2
    })

    assert b'Sucsess' in conf_opp.data


def test_view_marketplace(client: FlaskClient):
    now = (datetime.utcnow()
           ).strftime("%Y-%m-%dT%H:%M:%S")
    opps = client.post("/api/Opps", data={
        "x-access-token": stu_acc_token,
        "filterDate": now,
        "filterName": ""
    })

    assert b"1" in opps.data
    assert b"2" in opps.data


def test_book_opps(client: FlaskClient):
    # Opp 1
    book = client.post("/api/BookAnOpp", data={
        "x-access-token": stu_acc_token,
        "OppId": 1
    })

    assert b"Opportunity Booked." in book.data

    # Opp 2
    book = client.post("/api/BookAnOpp", data={
        "x-access-token": stu_acc_token,
        "OppId": 2
    })

    assert b"Opportunity Booked." in book.data


def test_view_booked_opps(client: FlaskClient):
    view_opps = client.post("/api/BookedOpps", data={
        "x-access-token": stu_acc_token
    })

    assert b"1" in view_opps.data
    assert b"2" in view_opps.data


def test_unbook_opp(client: FlaskClient):
    unbook = client.post("/api/UnBookAnOpp", data={
        "x-access-token": stu_acc_token,
        "OppId": 2
    })

    assert b"Opportunity UnBooked" in unbook.data


def test_view_my_opps(client: FlaskClient):
    my_opps = client.post("/api/MyOpps", data={
        "x-access-token": adm_acc_token
    })

    assert b"1" in my_opps.data

    my_opps = client.post("/api/MyOpps", data={
        "x-access-token": com_acc_token
    })

    assert b"2" in my_opps.data


def test_view_booked_students(client: FlaskClient):
    # Admin
    students = client.post("/api/BookedStudents", data={
        "x-access-token": adm_acc_token,
        "OppId": 1
    })

    assert b"1" in students.data

    # Community
    students = client.post("/api/BookedStudents", data={
        "x-access-token": com_acc_token,
        "OppId": 2
    })

    assert b"1" not in students.data


def test_get_opp_codes(client: FlaskClient):
    # Admin
    opp_code = client.post("/api/SignInStudents", data={
        "x-access-token": adm_acc_token,
        "OppId": 1
    })

    assert opp_code.status_code == 200
    global adm_clock_code
    adm_clock_code = opp_code.data

    # Community
    opp_code = client.post("/api/SignInStudents", data={
        "x-access-token": com_acc_token,
        "OppId": 2
    })

    assert opp_code.status_code == 200
    global com_clock_code
    com_clock_code = opp_code.data


def test_clock_in_out(client: FlaskClient):
    # Clock 1
    clock_in = client.post("/api/ClockInOut", data={
        "x-access-token": stu_acc_token,
        "QrCode": adm_clock_code
    })

    assert b"Thank you for clocking in, don't forget to clock out later" in clock_in.data

    clock_out = client.post("/api/ClockInOut", data={
        "x-access-token": stu_acc_token,
        "QrCode": adm_clock_code
    })

    assert b"You have completed the opportunty, the sponsor will be confirming your participation shortly." in clock_out.data

    # Clock 2
    clock_in = client.post("/api/ClockInOut", data={
        "x-access-token": stu_acc_token,
        "QrCode": com_clock_code
    })

    assert b"Thank you for clocking in, don't forget to clock out later" in clock_in.data

    clock_out = client.post("/api/ClockInOut", data={
        "x-access-token": stu_acc_token,
        "QrCode": com_clock_code
    })

    assert b"You have completed the opportunty, the sponsor will be confirming your participation shortly." in clock_out.data


def test_view_notifs(client: FlaskClient):
    notifs = client.post("/api/Notifications", data={
        "x-access-token": adm_acc_token
    })

    assert b"completed your opportunity" in notifs.data

    notifs = json.loads(notifs.data)
    global adm_msg_id
    adm_msg_id = notifs[0]['ID']

    notifs = client.post("/api/Notifications", data={
        "x-access-token": com_acc_token
    })

    assert b"completed your opportunity" in notifs.data

    notifs = json.loads(notifs.data)
    global com_msg_id
    com_msg_id = notifs[0]['ID']


def test_confirm_participation(client: FlaskClient):
    conf = client.post("/api/ConfParticipation", data={
        "x-access-token": adm_acc_token,
        "ID": adm_msg_id,
        "Hours": 5
    })

    assert b"Success, Hours Awarded" in conf.data

    conf = client.post("/api/ConfParticipation", data={
        "x-access-token": com_acc_token,
        "ID": com_msg_id,
        "Hours": 5
    })

    assert b"Success, Hours Awarded" in conf.data


def test_delete_opp(client: FlaskClient):
    del_opp = client.post("/api/DeleteOpp", data={
        "x-access-token": adm_acc_token,
        "OppId": 1
    })

    assert b"Opportunity Deleted" in del_opp.data

    del_opp = client.post("/api/DeleteOpp", data={
        "x-access-token": com_acc_token,
        "OppId": 2
    })

    assert b"Opportunity Deleted" in del_opp.data

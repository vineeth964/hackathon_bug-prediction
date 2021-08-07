from fastapi.testclient import TestClient
from main import app

from datetime import datetime,time

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if bug pred is true
def test_bug_pred_true():
    # defining a sample payload for the testcase
    payload = {
    "lines_of_code": 5550,
    "cyclomatic_complexity": 45,
    "essential_complexity": 43543,
    "design_complexity": 54645,
    "totalo_perators_operands": 234,
    "volume": 0,
    "program_length": 234,
    "difficulty": 0,
    "intelligence": 0,
    "effort": 0,
    "b": 0,
    "time_estimator": 23,
    "lOCode": 0,
    "lOComment": 0,
    "lOBlank": 0,
    "lOCodeAndComment": 2,
    "uniq_Op": 0,
    "uniq_Opnd": 22,
    "total_Op": 22,
    "total_Opnd": 333,
    "branchCount": 33,
    }
    with TestClient(app) as client:
        response = client.post("/predict_bug", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["defects"] == True

# test to check if bug pred is false
def test_bug_pred_false():
    # defining a sample payload for the testcase
    payload = {
    "lines_of_code": 0,
    "cyclomatic_complexity": 0,
    "essential_complexity": 0,
    "design_complexity": 0,
    "totalo_perators_operands": 234,
    "volume": 0,
    "program_length": 0,
    "difficulty": 0,
    "intelligence": 0,
    "effort": 0,
    "b": 0,
    "time_estimator": 0,
    "lOCode": 0,
    "lOComment": 0,
    "lOBlank": 0,
    "lOCodeAndComment": 0,
    "uniq_Op": 0,
    "uniq_Opnd": 0,
    "total_Op": 0,
    "total_Opnd": 0,
    "branchCount": 0,
    }
    with TestClient(app) as client:
        response = client.post("/predict_bug", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json()["defects"] == False

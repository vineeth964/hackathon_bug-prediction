import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict, retrain
from typing import List

# defining the main app
app = FastAPI(title="Bug Predictor", docs_url="/")

# calling the load_model during startup.
# this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload
class QueryIn(BaseModel):
    lines_of_code: float
    cyclomatic_complexity: float
    essential_complexity: float
    design_complexity : float
    totalo_perators_operands : float
    volume : float
    program_length : float
    difficulty : float
    intelligence  : float
    effort  : float
    b  : float 
    time_estimator  : float
    lOCode    : float
    lOComment : float
    lOBlank  : float
    lOCodeAndComment: float
    uniq_Op  : float
    uniq_Opnd  : float
    total_Op  : float
    total_Opnd : float
    branchCount : float


# class which is returned in the response
class QueryOut(BaseModel):
    defects : bool

# class which is expected in the payload while re-training
class FeedbackIn(BaseModel):
    lines_of_code: float
    cyclomatic_complexity: float
    essential_complexity: float
    design_complexity : float
    totalo_perators_operands : float
    volume : float
    program_length : float
    difficulty : float
    intelligence  : float
    effort  : float
    b  : float 
    time_estimator  : float
    lOCode    : float
    lOComment : float
    lOBlank  : float
    lOCodeAndComment: float
    uniq_Op  : float
    uniq_Opnd  : float
    total_Op  : float
    total_Opnd : float
    branchCount: float
    defects : bool

# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong"}


@app.post("/predict_bug", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the bug prediction value (200)
def predict_bug(query_data: QueryIn):
    output = {"defects": predict(query_data)}
    return output

@app.post("/feedback_loop", status_code=200)
# Route to further train the model based on user input in form of feedback loop
# Payload: FeedbackIn containing the code related parameters
# Response: Dict with detail confirming success (200)
def feedback_loop(data: List[FeedbackIn]):
    retrain(data)
    return {"detail": "Feedback loop successful"}



# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)

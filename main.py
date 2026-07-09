from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="AI CRM Backend")

# 1. PATIENT MODEL
class Patient(BaseModel):
    name: str
    phone: str
    last_visit: str
    problem: str

# 2. AI MESSAGE GENERATE - DUMMY VERSION
@app.post("/ai/generate-message/")
def generate_message(patient: Patient):
    # Billing illama test panradhuku dummy AI message
    ai_msg = f"Vanakkam {patient.name} avargale! Neenga last ah '{patient.problem}' ku vandhuteenga. Oru follow-up checkup ku vandhu ponga. Nandri - AI CRM"
    
    return {
        "patient_name": patient.name,
        "ai_message": ai_msg,
        "status": "success - dummy mode"
    }

# 3. TEST ROUTE
@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}

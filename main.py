from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import csv
from datetime import datetime

app = FastAPI()

# Allow frontend (HTML/JS) to send requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # or ["http://127.0.0.1:5500"] if you want specific origin
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend API is running"}

@app.post("/contact")
def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    message: str = Form(...)
):
    with open("contact_submissions.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), name, email, phone, message])
    return {"status": "success", "message": "Contact form submitted"}

@app.post("/hire")
def submit_hire_request():
    with open("hire_requests.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), "Hiring request received"])
    return {"status": "success", "message": "Successfully sent a hiring request!"}

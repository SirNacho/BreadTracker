from fastapi import FastAPI
from services.email_service import send_email
app = FastAPI()

@app.get('/')
async def root():
    return { 'message': 'Hello World' }

@app.get('/send-test-email')
async def send_test_email():
    send_email(
        "stevengia@outlook.com",  # change this
        "Test Email",
        "If you see this, it works."
    )
    return {"status": "Email sent"}
from supabase import create_client
import httpx
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Initialize Supabase client
supabase = create_client(url, key)

# Create HTTPX client for cookie management
client = httpx.Client()

def login(email, password):
    # Sign up the user (if not already signed up)
    signup_response = client.post(f"{url}/auth/v1/signup", json={
        "email": email,
        "password": password
    })

    if signup_response.status_code == 200:
        print("User signed up successfully.")
    else:
        print("Failed to sign up:", signup_response.json())

    # Log in the user
    login_response = client.post(f"{url}/auth/v1/token?grant_type=password", data={
        "email": email,
        "password": password
    })

    if login_response.status_code == 200:
        print("User logged in successfully.")
        session_data = login_response.json()
        # Extract the access token
        access_token = session_data['access_token']
        # Set the authorization header for subsequent requests
        client.headers.update({"Authorization": f"Bearer {access_token}"})
    else:
        print("Failed to log in:", login_response.json())

def insert_data(table_name, data):
    response = client.post(f"{url}/rest/v1/{table_name}", json=data)

    if response.status_code == 201:
        print("Data inserted successfully.")
    else:
        print("Failed to insert data:", response.json())

# Example usage
login(email, password)
insert_data("your_table_name", {"column1": "value1", "column2": "value2"})

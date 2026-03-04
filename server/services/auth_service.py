import os
from dotenv import load_dotenv
from supabase import create_client, AuthApiError

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_PROJECT_URL"), os.getenv("SUPABASE_API_KEY"))

def signup(email, password, first_name, last_name):
    try:
        return supabase.auth.sign_up({
            "email": email, "password": password,
            "options": {"data": {"first_name": first_name, "last_name": last_name}}
        })
    except AuthApiError as e:
        return f"Signup failed: {e.message}"

def login(email, password):
    try:
        return supabase.auth.sign_in_with_password({"email": email, "password": password})
    except AuthApiError as e:
        return f"Login failed: {e.message}"

def reset_password(new_password):
    try:
        return supabase.auth.update_user({"password": new_password})
    except AuthApiError as e:
        return f"Update failed: {e.message}"

def logout():
    try:
        return supabase.auth.sign_out()
    except AuthApiError as e:
        return f"Logout failed: {e.message}"
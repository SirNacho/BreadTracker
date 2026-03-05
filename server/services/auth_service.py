import os
from dotenv import load_dotenv
from supabase import create_client, AuthApiError

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_PROJECT_URL"), os.getenv("SUPABASE_API_KEY"))

def signup(email, password, first_name, last_name):
    # sign_up usually returns an AuthResponse object
    res = supabase.auth.sign_up({
        "email": email, 
        "password": password,
        "options": {"data": {"first_name": first_name, "last_name": last_name}}
    })
    
    # Check if the user was actually created
    if res.user is None:
        # If there's an error, it's usually in a specific field depending on the version
        return "Signup failed: Check if user already exists or password is too short"
    
    return res

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
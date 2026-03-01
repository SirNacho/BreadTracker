import os
from dotenv import load_dotenv
from supabase import create_client, Client

#Supabase Configurations Section
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError("The supabase url and key is not found. Something is wrong with the dotenv.")

supabase: Client = create_client(url, key)



#User Features Section

def create_user(email : str, password : str, first_name : str, last_name : str):
    try:
        response = supabase.auth.sign_up(
                {
                    "email" : email,
                    "password" : password,
                    "options" : {"data": {"first_name": first_name, "last_name" : last_name}}
                }
            )
        
        return response

    except Exception as e:
        print(f"Signup has failed: {e}")
        return None

def login_user(email : str, password : str):
    try:
        response = supabase.auth.sign_in_with_password(
                {
                    "email" : email,
                    "password" : password,
                }
            )
        
        return response

    except Exception as e:
        print(f"User login has failed: {e}")
        return None

def user_login_status():
    try:
        response = supabase.auth.get_user()
        
        if response.user:
            return True
        return False

    except Exception:
        return False

def change_user_password(new_password : str):

    if not user_login_status():
        print("Unable to change user password: unable to login the user.")
        return None

    try:
        response = supabase.auth.update_user(
                {
                    "password" : new_password,
                }
            )
        
        return response
    
    except Exception as e:
        print(f"Changing the user password has failed: {e}")
        return None

def logout_user():
    try:
        response = supabase.auth.sign_out()
        
        return response

    except Exception as e:
        print(f"Logging out user has failed: {e}")
        return None

def main():
    #create_user("test@example.com", "test123", "John", "Smith")
    #login_user("test@example.com", "test123")
    #change_user_password("test123")
    #logout_user()

if __name__ == "__main__":
    main()

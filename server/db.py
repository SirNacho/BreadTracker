import os
from dotenv import load_dotenv

from supabase import create_client, Client

#Supabase Configurations Section
load_dotenv()

url: str = os.environ.get("SUPABASE_PROJECT_URL")
key: str = os.environ.get("SUPABASE_API_KEY")

if not url or not key:
    raise ValueError("The supabase url and key is not found. Something is wrong with the dotenv.")

supabase: Client = create_client(url, key)
print("db.py has successfully created a supabase client connection!")

'''
This function, "loadSupabaseConnection(url, key)" is for in case front end needed a way to connect
the supabase connection without running db.py.
'''
def loadSupabaseConnection(url : str, key : str):
    if not url or not key:
        raise ValueError("The supabase url and key is not found. Something is wrong with either the inputted parameters.")

    try:
        supabase: Client = create_client(url, key)
        print("Supabase client has successfully been created!")
    except Exception as e:
        print(f"The supabase client is unable to be created. Check what's up with the url and api key.")
        return None


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

    #Example usage:
    #create_user("test@example.com", "test123", "John", "Smith")
    #login_user("test@example.com", "test123")
    #change_user_password("test123")
    #logout_user()

    print("This db.py code has run! Please feel free to look at main() to see how to use the functions in db.py!")

if __name__ == "__main__":
    main()

'''
Not sure what this code below is for. I'll leave this here just in case. -SF
'''

'''
from sqlmodel import create_engine, Session, SQLModel

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
'''

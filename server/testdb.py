import os
from dotenv import load_dotenv
from supabase import create_client, Client

#Features to work on:
#- Create a user
#- Login using email and password
#: Logout
#: Change password

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise ValueError("The supabase url and key is not found. Something is wrong with the dotenv.")

supabase: Client = create_client(url, key)

def main():
    print("Hi, I'm working")

    testPrintSubscription = (
            supabase.table("subscriptions")
            .select("*")
            .execute()
            )
    print("Response: {}".format(testPrintSubscription))


if __name__ == "__main__":
    main()

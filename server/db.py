import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv('CONNECTION_STRING')

engine = create_engine(CONNECTION_STRING, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
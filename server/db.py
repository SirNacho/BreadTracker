import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL, 
    echo=True, 
    future=True
)

SessionLocal = sessionmaker(
    bind=engine, 
    autocommit=False, 
    autoflush=False, 
    class_=Session
)

def get_session():
    with SessionLocal() as session:
        yield session
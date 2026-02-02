from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from contextlib import asynccontextmanager

from db import create_db_and_tables
from routes import grocery_list
import models

load_dotenv()

origins = [
    'http://localhost:3000',
    'http://192.168.1.144:3000'
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    pass    

app = FastAPI(lifespan=lifespan)

app.include_router(grocery_list.router, prefix='/grocery-list', tags=['grocery-list'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/ping')
def ping():
    return { 'message': 'pong' }
from fastapi import APIRouter, FastAPI
from routes.subscription_api import router as subs_router
from routes.auth_api import router as auth_router

app = FastAPI()

@app.get('/')
async def root():
    return { 'message': 'BreadTracker API is Online' }

api_router = APIRouter(prefix='/api')

api_router.include_router(subs_router)
api_router.include_router(auth_router)

app.include_router(api_router)
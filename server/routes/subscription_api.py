from db import get_session
from fastapi import APIRouter
from models import Subscription
from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from schemas import CreateSubscriptionRequest, UpdateSubscriptionRequest
# from schemas.requests.subscription_requests import UpdateSubscriptionRequest

router = APIRouter(prefix='/subscription', tags=['Subscriptions'])

@router.get('/')
def get_subscriptions(session: Session = Depends(get_session)):
    statement = select(Subscription)
    results = session.exec(statement)
    return results.all()

@router.get('/{id}')
def get_subscription(id: int, session: Session = Depends(get_session)):
    subscription = session.get(Subscription, id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.post('/create')
def create_subscription(request: CreateSubscriptionRequest, session: Session = Depends(get_session)):
    subscription = Subscription.model_validate(request)
    session.add(subscription)
    
    try:
        session.commit()
        session.refresh(subscription)
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    
    return subscription

@router.post('/update/{id}')
def update_subscription(id: int, request: UpdateSubscriptionRequest, session: Session = Depends(get_session)):
    subscription = session.get(Subscription, id)
    
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    update_data = request.model_dump(exclude_unset=True)
    print(f"DEBUG: update_data keys are: {list(update_data.keys())}")
    print(f"DEBUG: Subscription object attributes are: {subscription.__dict__.keys()}")
    
    subscription.sqlmodel_update(update_data)
    
    session.add(subscription)
    session.commit()
    session.refresh(subscription)
    
    return subscription
    
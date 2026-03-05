import uuid 
from pydantic import EmailStr
from typing import List, Optional
from models.subscription import Subscription
from sqlmodel import Field, Relationship, SQLModel


class Profile(SQLModel, table=True):
    __tablename__ = 'profiles'
    
    user_id: uuid.UUID = Field(primary_key=True)
    email: EmailStr = Field(index=True, unique=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
    
    subscriptions: List["Subscription"] = Relationship(back_populates="user")
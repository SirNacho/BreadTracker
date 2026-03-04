from typing import List, Optional
from pydantic import EmailStr
from sqlmodel import UUID, Field, Relationship, SQLModel

from models.subscription import Subscription


class Profile(SQLModel, table=True):
    __tablename__ = 'profiles'
    
    id: UUID = Field(primary_key=True)
    email: EmailStr = Field(index=True, unique=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
    
    subscriptions: List[Subscription] = Relationship(back_populates="user")
from cProfile import Profile
from datetime import datetime
from typing import Optional
from sqlmodel import UUID, Field, Relationship, SQLModel, Column, DateTime, func

class Subscription(SQLModel, table=True):
    __tablename__ = "subscriptions"
    
    subscription_id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str = Field(nullable=False)
    cost: float = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    user_id: UUID = Field(foreign_key='profiles.id')
    created_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), 
            server_default=func.now(),
            nullable=False
        )
    )
    modified_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True), 
            server_default=func.now(),
            nullable=False
        )
    )
    
    user: Profile = Relationship(back_populates='subscriptions')
    
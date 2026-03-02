from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Column, DateTime, func

class Subscription(SQLModel, table=True):
    __tablename__ = "subscriptions"
    
    subscription_id: Optional[int] = Field(default=None, primary_key=True)
    subscription_service_name: str = Field(nullable=False)
    subscription_cost: float = Field(nullable=False)
    is_active: bool = Field(default=True, nullable=False)
    
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            server_default=func.now(),
            nullable=False
        )
    )
    modified_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), 
            server_default=func.now(),
            nullable=False
        )
    )
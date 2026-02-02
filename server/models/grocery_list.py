from datetime import datetime
from typing import Optional, Dict, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB

from schemas.responses import GroceryOption

class GroceryList(SQLModel, table=True):
    __tablename__: str = 'grocery_lists'
    
    grocery_list_id: Optional[int] = Field(default=None, primary_key=True)
    contents: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    grocery_options: Dict[str, List[GroceryOption]] = Field(
        default_factory=dict,
        sa_column=Column(JSONB, nullable=True)
    )
    created_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    ))
    modified_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    ))
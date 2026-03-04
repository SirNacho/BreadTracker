from typing import Optional

from pydantic import EmailStr
from sqlmodel import UUID, Field, SQLModel


class Profile(SQLModel, table=True):
    __tablename__ = 'profiles'
    
    id: UUID = Field(primary_key=True)
    email: EmailStr = Field(index=True, unique=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None
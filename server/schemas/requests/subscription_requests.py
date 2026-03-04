from typing import Optional
from ..SqlCamelModel import SqlCamelModel

class CreateSubscriptionRequest(SqlCamelModel):
    service_name: str
    cost: float

class UpdateSubscriptionRequest(SqlCamelModel):
    service_name: Optional[str] = None
    cost: Optional[float] = None
    is_active: Optional[bool] = None
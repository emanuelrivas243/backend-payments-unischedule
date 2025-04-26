from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional
from enum import Enum as PyEnum

class PaymentBase(BaseModel):
    user_id: int
    amount: float
    currency: str = Field(..., min_length=3, max_length=3)

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdateStatus(BaseModel):
    class StatusEnum(str, PyEnum):
        pending = "pending"
        completed = "completed"
        cancelled = "cancelled"
        failed = "failed"

    status: StatusEnum

class PaymentResponse(PaymentBase):
    payment_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
import uuid
from sqlalchemy import Column, Integer, Numeric, String, DateTime, Enum, UUID
from sqlalchemy.sql import func

from database import Base 
# ----------------------------------------

import enum
class PaymentStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    cancelled = "cancelled"
    failed = "failed"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    payment_id = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    user_id = Column(Integer, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    currency = Column(String(3), nullable=False)
    status = Column(Enum(PaymentStatus, name="payment_status"),
                    nullable=False, default=PaymentStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    def __repr__(self):
        return f"<Payment(payment_id={self.payment_id}, status='{self.status}', amount={self.amount})>"
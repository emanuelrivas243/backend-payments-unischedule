from sqlalchemy.orm import Session
from uuid import UUID
from typing import List


import models
import schemas
from models import PaymentStatus

# -------------------------------------------

def get_payment(db: Session, payment_id: UUID):
    # Accedemos al modelo Payment a través del módulo models importado
    return db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()

def get_payments(db: Session, skip: int = 0, limit: int = 100) -> List[models.Payment]:
    # Accedemos al modelo Payment a través del módulo models importado
    return db.query(models.Payment).offset(skip).limit(limit).all()

def create_payment(db: Session, payment: schemas.PaymentCreate) -> models.Payment:
    # Creamos una instancia del modelo Payment, accediendo a él a través del módulo models
    db_payment = models.Payment(
        user_id=payment.user_id,
        amount=payment.amount,
        currency=payment.currency
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def update_payment_status(db: Session, payment: models.Payment, status: str) -> models.Payment:

    # Para asignar el nuevo estado al objeto Payment
    payment.status = status
    db.commit()
    db.refresh(payment)
    return payment

def delete_payment(db: Session, payment: models.Payment):
    db.delete(payment)
    db.commit()
    pass
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

import crud
import models 
import schemas 

# Dependencia directa de la DB
from database import get_db
# -------------------------------------------

router = APIRouter(
    prefix="/payments",
    tags=["payments"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PaymentResponse)
def create_payment(
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db)
):
    # Accedemos a la función create_payment a través del módulo crud importado
    db_payment = crud.create_payment(db=db, payment=payment)
    return db_payment

@router.get("/", response_model=List[schemas.PaymentResponse])
def read_payments(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    # Accedemos a la función get_payments a través del módulo crud importado
    payments = crud.get_payments(db, skip=skip, limit=limit)
    return payments

@router.get("/{payment_id}", response_model=schemas.PaymentResponse)
def read_payment(
    payment_id: UUID,
    db: Session = Depends(get_db)
):
    # Accedemos a la función get_payment a través del módulo crud importado
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")
    return db_payment

@router.patch("/{payment_id}/status", response_model=schemas.PaymentResponse)
def update_payment_status(
    payment_id: UUID,
    status_update: schemas.PaymentUpdateStatus,
    db: Session = Depends(get_db)
):
    # Primero obtenemos el pago usando la función del módulo crud
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    # Luego llamamos a la función de actualización a través del módulo crud
    updated_payment = crud.update_payment_status(db=db, payment=db_payment, status=status_update.status.value)
    return updated_payment

@router.delete("/{payment_id}")
def delete_payment(
     payment_id: UUID,
     db: Session = Depends(get_db)
):
    # Primero obtenemos el pago usando la función del módulo crud
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    # Luego llamamos a la función de eliminación a través del módulo crud
    crud.delete_payment(db=db, payment=db_payment)
    return {"message": "Payment deleted successfully", "payment_id": payment_id}

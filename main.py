from fastapi import FastAPI

from database import engine, Base 
from routers import payments 



try:
    print("Intentando crear tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas (o ya existían) exitosamente.")
except Exception as e:
    print(f"Error al intentar crear tablas: {e}")

# Crea la instancia de la aplicación FastAPI
app = FastAPI(
    title="Payment Microservice",
    description="Simple CRUD microservice for managing payment records.",
    version="1.0.0",
)


app.include_router(payments.router)


@app.get("/")
def read_root():
    return {"message": "Payment microservice is running"}
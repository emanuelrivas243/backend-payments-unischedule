from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 


from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv


# Cargar variables de entorno del archivo .env
load_dotenv()


# Obtener la URL de la base de datos de las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise EnvironmentError("La variable de entorno DATABASE_URL no está configurada.")

# Configurar el motor de la base de datos
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Asegúrate de cerrar la sesión
#backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import os

#URL de connexion à la bdd
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

#création de l'engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

#session de la bdd
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

#dépendance pour obtenir session de bdd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse

router = APIRouter()

# Endpoint GET - récupérer toutes les donations
@router.get("/donations")
def get_donations(db: Session = Depends(get_db)):
    try:
        donations = db.execute("SELECT * FROM donation").fetchall()
        return donations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint GET - récupérer une donation par ID
@router.get("/donations/{donation_id}")
def get_donation(donation_id: int, db: Session = Depends(get_db)):
    try:
        donation = db.execute("SELECT * FROM donation WHERE id = :id", {"id": donation_id}).fetchone()
        if not donation:
            raise HTTPException(status_code=404, detail="Donation not found")
        return donation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Endpoint POST - pour add une donation
@router.post("/donations")
def create_donation(data: dict, db: Session = Depends(get_db)):
    try:
        query = "INSERT INTO donation (field1, field2) VALUES (:field1, :field2)"
        db.execute(query, data)
        db.commit()
        return {"detail": "Donation created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Endpoint PUT - maj une donation
@router.put("/donations/{donation_id}")
def update_donation(donation_id: int, data: dict, db: Session = Depends(get_db)):
    try:
        query = "UPDATE donation SET field1 = :field1, field2 = :field2 WHERE id = :id"
        result = db.execute(query, {"id": donation_id, **data})
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Donation not found")
        db.commit()
        return {"detail": "Donation updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint DELETE - supprimer une donation
@router.delete("/donations/{donation_id}")
def delete_donation(donation_id: int, db: Session = Depends(get_db)):
    try:
        query = "DELETE FROM donation WHERE id = :id"
        result = db.execute(query, {"id": donation_id})
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Donation not found")
        db.commit()
        return {"detail": "Donation deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Endpoint POST - pour add un user
@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Endpoint GET - pour récupérer tous les users
@router.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

#Endpoint GET - récupérer un user par ID
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Endpoint PUT - maj d'un user
@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

#Endpoint DELETE - supprimer un user
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}


from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


class AuthService:

    @staticmethod
    def register_user(db: Session, data: UserCreate) -> User:

        existing_email = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if existing_email:
            raise ValueError("Email already registered.")

        existing_username = (
            db.query(User)
            .filter(User.username == data.username)
            .first()
        )

        if existing_username:
            raise ValueError("Username already taken.")

        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
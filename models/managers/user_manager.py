from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from config import engine
from models import User, Role


class UserManager:
    def __init__(self):

        self.Session = sessionmaker(bind=engine)
        # Создаем контекст для хеширования с настройками безопасности
        self.pwd_context = CryptContext(
            schemes=["argon2"],
            deprecated="auto"
        )

    def _hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def add_user(self, db: Session, username: str, email: str, role: Role, password: str) -> User:
        # Проверка на существование пользователя
        existing_user = db.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()

        if existing_user:
            if existing_user.username == username:
                raise ValueError("Username already exists.")
            else:
                raise ValueError("Email already exists.")

        # Хеширование пароля перед сохранением
        hashed_password = self._hash_password(password)

        # Создание нового пользователя
        new_user = User(
            username=username,
            email=email,
            role=role,
            password=hashed_password
        )

        db.add(new_user)
        return new_user

    def get_user_by_id(self, user_id):
        with self.Session() as session:
            return session.query(User).get(user_id)

    def update_user(self, session, user_id, updated_data):
        """Update an existing user."""
        user = session.query(User).get(user_id)
        if not user:
            return False

        for key, value in updated_data.items():
            if value is not None:
                setattr(user, key, value)

        session.commit()
        return user

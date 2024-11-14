from sqlalchemy.orm import sessionmaker
from config import engine
from models import User, Role
from passlib.context import CryptContext


class UserManager:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        # Create context for password hashing with security settings
        self.pwd_context = CryptContext(
            schemes=["argon2"],
            deprecated="auto"
        )

    def _hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def add_user(self, db, username: str, email: str, role: Role, password: str) -> User:
        # Check if the user already exists
        with self.Session() as session:
            existing_user = session.query(User).filter(
                (User.username == username) | (User.email == email)
            ).first()

            if existing_user:
                if existing_user.username == username:
                    raise ValueError("Le nom d'utilisateur existe déjà.")  # "Username already exists."
                else:
                    raise ValueError("L'email existe déjà.")  # "Email already exists."

            # Hash the password before saving
            hashed_password = self._hash_password(password)

            # Create a new user
            new_user = User(
                username=username,
                email=email,
                role=role,
                password=hashed_password
            )

            session.add(new_user)
            session.commit() 
            session.refresh(new_user)  
            return new_user

    def get_user_by_id(self, db, user_id: int):
        """Retrieve user by ID."""
        with self.Session() as session:
            return session.query(User).get(user_id)

    def get_all_users(self, db):
        """Get all users."""
        with self.Session() as session:
            return session.query(User).all()

    def update_user(self, db, user_id: int, updated_data: dict):
        """Update user data by ID."""
        with self.Session() as session:
            user = session.query(User).get(user_id)
            
            if not user:
                return None

            # Update user fields
            for key, value in updated_data.items():
                if value is not None:
                    setattr(user, key, value)

            session.commit()  
            return user

    def delete_user(self, db, user_id):
        """Delete an existing user."""
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False
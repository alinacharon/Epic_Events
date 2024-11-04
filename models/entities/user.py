from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class Role(enum.Enum):
    ADMIN = 'ADMIN'
    MANAGEMENT = 'MANAGEMENT'
    COMMERCIAL = 'COMMERCIAL'
    SUPPORT = 'SUPPORT'

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Role))
    clients = relationship("Client", back_populates="commercial")

    def __repr__(self):
        return f"<User {self.username}>"
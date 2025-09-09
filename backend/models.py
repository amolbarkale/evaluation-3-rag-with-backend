from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    documents = relationship("Document", back_populates="user")

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    content = Column(String)
    user = relationship("User", back_populates="documents")

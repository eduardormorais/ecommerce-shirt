from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from app.config.db import database


class User(database.Model, SerializerMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    fullname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String, nullable=False)

    def __init__(self, fullname, password, email, cpf):
        self.fullname = fullname
        self.password = password
        self.email = email
        self.cpf = cpf

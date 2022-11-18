from typing import Any

from app.modules.user.model import User
from app.config.db import database


class UserRepository:
    def __init__(self):
        self.__session = database.session

    def insert(self, user: User):
        self.__session.add(user)
        self.__session.commit()
        return True

    def delete(self):
        pass

    def select_all(self) -> []:
        users = self.__session.query(User).all()
        return users

    def find_by_id(self, id: int) -> User | None:
        user = self.__session.query(User).filter(User.id == id).first()
        if user:
            return user
        return None

    def find_by_email(self, email: str) -> User | None:
        user = self.__session.query(User).filter(User.email == email).first()
        if user:
            return user
        return None

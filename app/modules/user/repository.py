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

    def select_all(self):
        users = self.__session.query(User).all()
        list_users = [user.to_dict() for user in users]
        return list_users

    def select_by_id(self, id: int):
        user = self.__session.query(User).filter(User.id == id).first()
        user_dict = user.to_dict()
        return user_dict

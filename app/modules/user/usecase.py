from app.modules.core import utils
from app.modules.core.enum import MessageEnum
from app.modules.user.model import User
from app.modules.user.repository import UserRepository


class GetOneUserUseCase:
    def __init__(self, id: int):
        self.__repository = UserRepository()
        self.__id = id

    def execute(self):
        return self.__repository.select_by_id(self.__id)


class GetAllUsersUseCase:
    def __init__(self):
        self.__repository = UserRepository()

    def execute(self):
        return self.__repository.select_all()


class RegisterUserUsecase:
    def __init__(self, payload):
        self.__payload = payload
        self.__repository = UserRepository()

    def __validate(self):
        utils.valid_email(self.__payload["email"])
        utils.valid_name(self.__payload["fullname"])
        utils.valid_password(self.__payload["password"])
        utils.valid_cpf(self.__payload["cpf"])

    def __register_user(self):
        user = User(**self.__payload)
        self.__repository.insert(user)
        return user

    def execute(self):
        self.__validate()
        user = self.__register_user()
        return {"detail": MessageEnum.USER_REGISTRED.value, "user": user.to_dict()}


class UpdateUserUseCase:
    pass


class DeleteUserUseCase:
    pass

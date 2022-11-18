from app.modules.core.enum import MessageEnum
from app.modules.core.exceptions import InvalidData
from app.modules.user.model import User
from app.modules.user.repository import UserRepository
from app.modules.user.schema import CreateUserSchema
from marshmallow.exceptions import ValidationError


class GetOneUserUseCase:
    def __init__(self, id: int):
        self.__repository = UserRepository()
        self.__id = id

    def __validate(self):
        user = self.__repository.find_by_id(id=self.__id)
        if not user:
            raise InvalidData(detail="Usuário não encontrado.", status_code=404)
        return user.to_dict()

    def execute(self):
        user_dict = self.__validate()
        return user_dict


class GetAllUsersUseCase:
    def __init__(self):
        self.__repository = UserRepository()

    def execute(self):
        users = self.__repository.select_all()
        list_users = [user.to_dict() for user in users]
        return list_users


class RegisterUserUsecase:
    def __init__(self, payload):
        self.__payload = payload
        self.__repository = UserRepository()
        self.__create_user_serializer = CreateUserSchema()

    def __verify_payload(self):
        try:
            user_schema = self.__create_user_serializer.load(self.__payload)
            return user_schema
        except ValidationError as exc:
            raise InvalidData(detail=exc, status_code=400)

    def __verify_user_exists(self, user_schema: dict):
        if self.__repository.find_by_email(user_schema.get("email")):
            raise InvalidData(detail="Email já cadastrado.", status_code=400)

    def __validate(self):
        user_schema = self.__verify_payload()
        self.__verify_user_exists(user_schema)
        return user_schema

    def __register_user(self, user_schema: dict):
        user = User(**user_schema)
        self.__repository.insert(user)
        return user

    def execute(self):
        user_schema = self.__validate()
        user = self.__register_user(user_schema)
        return {"detail": MessageEnum.USER_REGISTRED.value, "user": user.to_dict()}


class UpdateUserUseCase:
    pass


class DeleteUserUseCase:
    pass

from flask import Blueprint, jsonify
from flask import request
from starlette import status

from app.modules.user.usecase import (
    RegisterUserUsecase,
    GetAllUsersUseCase,
    GetOneUserUseCase,
)

bp = Blueprint("user", __name__)


@bp.route("/api/user", methods=["GET"])
def get_all_users():
    list_users = GetAllUsersUseCase().execute()
    return jsonify(list_users), status.HTTP_200_OK


@bp.route("/api/user", methods=["POST"])
def create_user():
    payload = request.json
    result = RegisterUserUsecase(payload).execute()
    return result, status.HTTP_201_CREATED


@bp.route("/api/user/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    result = GetOneUserUseCase(user_id).execute()
    return result, status.HTTP_200_OK

from flask_sqlalchemy.model import Model
from sqlalchemy_serializer import SerializerMixin
from app.modules.user.model import User


def test_user_model(user_faker_dict):
    user = User(**user_faker_dict)

    assert isinstance(user, Model)
    assert isinstance(user, SerializerMixin)

    obj_dict = user.to_dict()
    for key in user_faker_dict.keys():
        assert obj_dict[key] == user_faker_dict[key]

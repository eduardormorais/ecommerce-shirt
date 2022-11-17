import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture(scope="module")
def user_faker_dict():
    return {
        "fullname": faker.name(),
        "password": faker.password(length=8),
        "email": faker.free_email(),
        "cpf": faker.cpf(),
    }

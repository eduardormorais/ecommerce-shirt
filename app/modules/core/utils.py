import re
from pycpfcnpj import cpfcnpj
from app.modules.core.exceptions import InvalidData


def valid_cpf(cpf_value):
    if not cpfcnpj.validate(cpf_value):
        raise InvalidData(
            status_code=400,
            detail="CPF inválido.",
        )


def valid_email(email):
    if not valid_string_format_email(email):
        raise InvalidData(detail="E-mail inválido", status_code=400)


def valid_name(name: str):
    if not valid_string_any_less_characters(name, 5):
        raise InvalidData(
            status_code=400,
            detail="Nome precisa ter pelo menos 5 letas.",
        )
    if not valid_number_of_words_string(name, 2):
        raise InvalidData(
            status_code=400,
            detail="É necessário informar um segundo nome.",
        )


def valid_password(password):
    if not valid_string_any_less_characters(password, 8):
        raise InvalidData(
            status_code=400,
            detail="Senha precisa ter pelo menos 8 characteres.",
        )
    if not valid_string_with_number(password):
        raise InvalidData(
            status_code=400,
            detail="Senha precisa ter pelo menos 1 numero.",
        )
    if not valid_string_with_upper_case(password):
        raise InvalidData(
            status_code=400,
            detail="Senha precisa ter  ao menos 1 letra maiúscula",
        )
    if not valid_string_with_lower_case(password):
        raise InvalidData(
            status_code=400,
            detail="Senha precisa ter  ao menos 1 letra minuscula",
        )
    if not valid_string_with_special_character(password):
        raise InvalidData(
            status_code=400,
            detail="Senha precisa ter ao menos 1 character especial.",
        )


def valid_number_of_words_string(string, number_words):
    str_split = string.split()
    if len(str_split) < number_words:
        return False
    return True


def valid_string_format_email(email: str):
    regex = r"[^@]+@[^@]+\.[^@]+"
    if not re.match(regex, email):
        return False
    return True


def valid_string_any_less_characters(string: str, max_characters: int):
    print(string, len(string), len(string) < max_characters)
    if len(string) < max_characters:
        return False
    return True


def valid_string_with_number(password: str):
    if not re.findall(r"\d", password):
        return False
    return True


def valid_string_with_upper_case(password: str):
    if not re.findall(r"[A-Z]", password):
        return False
    return True


def valid_string_with_lower_case(password: str):
    if not re.findall(r"[a-z]", password):
        return False
    return True


def valid_string_with_special_character(password: str):
    if not re.findall(r"[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]", password):
        return False
    return True

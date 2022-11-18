from werkzeug.exceptions import HTTPException


class InvalidData(HTTPException):

    def __init__(self, detail, status_code, payload=None):
        super().__init__()
        self.description = detail
        self.payload = payload
        self.code = status_code

    def to_dict(self):
        return {
            "status_code": self.code,
            "description": self.description,
        }

class InvalidData(Exception):
    def __init__(self, detail, status_code, payload=None):
        super().__init__()
        self.detail = detail
        self.payload = payload
        self.status_code = status_code

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["detail"] = self.detail
        return rv

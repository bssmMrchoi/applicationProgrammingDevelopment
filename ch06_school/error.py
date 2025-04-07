class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
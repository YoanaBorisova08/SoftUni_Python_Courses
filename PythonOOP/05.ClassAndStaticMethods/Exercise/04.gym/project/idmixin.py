class IDMixin:
    ID: int = 1

    @classmethod
    def get_next_id(cls):
        return cls.ID

    @classmethod
    def increment_id(cls):
        cls.ID += 1
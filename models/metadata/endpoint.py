from enum import Enum


class Endpoint(Enum):
    @classmethod
    def isin(cls, value):
        return value in cls._value2member_map_

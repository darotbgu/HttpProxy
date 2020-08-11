from enum import IntEnum


class RuleType(IntEnum):
    SOURCE_IP = 1
    SOURCE_USER = 2
    DESTINATION_HOST = 3
    DESTINATION_PORT = 4
    DESTINATION_METHOD = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

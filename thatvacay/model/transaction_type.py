from enum import Enum


class TransactionType(Enum):
    TRANSFER = "TRANSFER"
    SPENDING = "SPENDING"
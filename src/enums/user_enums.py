from enum import Enum


class Genders(Enum):
    male = "male"
    female = "female"


class Statuses(Enum):
    inactive = "inactive"
    active = "active"


class UserError(Enum):
    WRONG_EMAIL = "Email doesn`t contain @"

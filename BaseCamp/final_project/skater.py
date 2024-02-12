from datetime import date, datetime
from typing import List

class Skater:
    def __init__(self, id: int, first_name: str, last_name: str, nationality: str, gender: str, date_of_birth: date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.gender = gender
        self.date_of_birth = date_of_birth

    def get_age(self, date: date = date.today()) -> int:
        birth_date = self.date_of_birth
        age = date.year - birth_date.year - ((date.month, date.day) < (birth_date.month, birth_date.day))
        return age

    def get_events(self):
        # Implement logic to retrieve events associated with this skater
        pass

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__, ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

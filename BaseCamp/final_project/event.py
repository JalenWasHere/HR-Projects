from datetime import date, datetime
from typing import List


class Event:
    def __init__(self, id: int, name: str, track_id: int, date: date, distance: int, duration: float, laps: int,
                 winner: str, category: str):
        self.id = id
        self.name = name
        self.track_id = track_id
        self.date = date
        self.distance = distance
        self.duration = duration
        self.laps = laps
        self.winner = winner
        self.category = category

    def add_skater(self, skater: 'Skater'):
        # Implement logic to add skater to event_skaters table
        pass

    def get_skaters(self) -> List['Skater']:
        # Implement logic to retrieve skaters associated with this event
        pass

    def get_track(self) -> 'Track':
        # Implement logic to retrieve the Track object associated with this event
        pass

    def convert_date(self, to_format: str) -> str:
        # Implement logic to convert event date to the provided format
        pass

    def convert_duration(self, to_format: str) -> str:
        # Implement logic to convert event duration to the provided format
        pass

    def __repr__(self) -> str:
        return "{}({})".format(type(self).__name__,
                               ", ".join([f"{key}={value!s}" for key, value in self.__dict__.items()]))

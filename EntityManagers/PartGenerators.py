from WorkFlow.helpers import is_delay, get_part
import random
from data_store import DELAY_PERCENTAGE
from Entities.Part import Part
from data_store import ALLOWED_KEYS


class PartGenerator:
    """
    Singleton Class
    This will resemble Line A, Line B and Line C
    At any instance, it will mention if part A, B or C will be generated.
    Allowed Keys for the kwargs so far are:
        interval_A, interval_B, interval_C
    intervals are passed in minutes
    """
    def __init__(self, interval_A: int,
                 interval_B: int, interval_C: int):
        self.parts = ["A", "B", "C"]
        self.intervals = [
            interval_A * 60,
            interval_B * 60,
            interval_C * 60
        ]
        self.start_time = 0
        self.__last_release_time_point = [0] * 3
        self.__delays = [(False, 0)] * 3

    def get_parts(self, current_time: int):
        are_parts_delayed = is_delay(self.parts)
        for index, a_part_type in enumerate(self.parts):
            part_release_point = self.__last_release_time_point[0] + self.interval_A
            if part_release_point >= current_time:
                self.__last_release_time_point[0] = part_release_point
                yield get_part(a_part_type)

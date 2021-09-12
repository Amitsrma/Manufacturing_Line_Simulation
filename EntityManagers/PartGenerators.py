import random
from data_store import 
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
    def __init__(self, start_time: int, interval_A: int,
                 interval_B: int, interval_C: int):
        self.interval_A = interval_A * 60
        self.interval_B = interval_B * 60
        self.interval_C = interval_C * 60
        self.start_time = start_time
        self.__time_waited = [start_time] * 3
        self.__delays = [(False, 0)] * 3

    def get_parts(self, current_time: int):
        pass

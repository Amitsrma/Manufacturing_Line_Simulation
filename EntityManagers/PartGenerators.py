from typing import List
from WorkFlow.helpers import is_delay, get_part
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
    def __init__(self, part_A: Part,
                 part_B: Part, part_C: Part):
        self.parts = ["A", "B", "C"]
        self.intervals = [
            part_A.arrival_time_interval * 60,
            part_B.arrival_time_interval * 60,
            part_C.arrival_time_interval * 60
        ]
        self.start_time = 0
        self.__last_release_time_point = [0] * 3
        self.__delays = [(False, 0)] * 3

    def get_parts(self, current_time: int) -> List[Part]:
        generated_parts = []
        for index, a_part_type in enumerate(self.parts):
            part_release_point = self.__last_release_time_point[0] + self.intervals[index]
            if not self.__delays[index][0]:  # delay has not occured
                self.__delays[index] = is_delay(part_type=a_part_type)
            part_release_point += self.__delays[index][1]
            if part_release_point >= current_time:
                self.__last_release_time_point[0] = part_release_point
                self.__delays[index] = (False, 0)
                generated_parts.append(get_part(a_part_type))
            else:
                generated_parts.append(None)
        return generated_parts

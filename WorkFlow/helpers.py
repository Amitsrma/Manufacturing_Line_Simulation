from data_store import DELAY_DISTRIBUTION, DELAY_PERCENTAGE, INTERVALS
from Entities.Part import Part
import random
from typing import Tuple


def wait_time_from_triangle_distribution(distribution: Tuple[int, int, int]) -> int:
    """
    Get wait time for a given triangular distribution.

    params:
        distribution: Tuple of integer (min, mode, max) values

    returns: integer that gives wait time for given distribution
    """
    min = distribution[0]
    mode = distribution[1]
    max = distribution[2]
    interval_to_wait = random.triangular(low=min, mode=mode, high=max)
    return int(interval_to_wait)


def wait(start_time: int, wait_interval: int):
    """
    Allows parallel execution of the process while system's
    individual entities are processing/working/blocking the
    system.
    """
    # TODO identify if synchronous/asynchronous solution would work here
    raise NotImplementedError


def is_delay(part_type: str) -> Tuple[bool, int]:
    """
    For a given part type, returns if there will be delay.

    Params:
        part_type: a string that denotes the type of part

    returns: bool
    """
    delay_threshold = DELAY_PERCENTAGE.get(part_type)
    if random.random() < delay_threshold:
        delayed_by = wait_time_from_triangle_distribution(
            distribution=DELAY_DISTRIBUTION.get(part_type)
            )
        flag = True
    else:
        delayed_by = 0
        flag = False
    return flag, delayed_by


def get_part(part_type: str) -> Part:
    return Part(
        part_type=part_type,
        arrival_time_interval=INTERVALS.get(part_type),
        delay_percentage=DELAY_PERCENTAGE.get(part_type)
    )

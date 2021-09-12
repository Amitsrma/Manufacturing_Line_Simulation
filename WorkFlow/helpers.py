from data_store import DELAY_PERCENTAGE
import random
from typing import Tuple


def wait_time_from_triangle_distribution(distribution: Tuple[int, int, int]) -> int:
    """
    Get wait time for a given triangular distribution.

    params:
        distribution: Tuple of integer (min, mode, max) values
    
    returns: integer that gives wait time for given distribution
    """
    interval_to_wait = random.triangular(distribution)
    return int(interval_to_wait)


def wait(start_time: int, wait_interval: int):
    """
    Allows parallel execution of the process while system's
    individual entities are processing/working/blocking the
    system.
    """
    # TODO identify if synchronous/asynchronous solution would work here
    raise NotImplementedError


def is_delay(part_type: str) -> bool:
    """
    For a given part type, returns if there will be delay.

    Params:
        part_type: a string that denotes the type of part

    returns: bool
    """
    delay_threshold = DELAY_PERCENTAGE.get(part_type)
    if random.random() < delay_threshold:
        return True
    return False

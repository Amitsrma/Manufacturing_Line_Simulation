from data_store import DELAY_DISTRIBUTION, DELAY_PERCENTAGE, INTERVALS
from Entities.Part import Part
import random
from typing import List, Tuple


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


def is_delay(part_types: List[str]) -> bool:
    """
    For a given part type, returns if there will be delay.

    Params:
        part_type: a string that denotes the type of part

    returns: bool
    """
    delays = []
    for a_part_type in part_types:
        delay_threshold = DELAY_PERCENTAGE.get(a_part_type)
        if random.random() < delay_threshold:
            delayed_by = wait_time_from_triangle_distribution(
                distribution=DELAY_DISTRIBUTION.get(a_part_type)
                )
            delays.append((True, delayed_by))
        else:
            delays.append(False, 0)
    return delays


def get_part(part_type: str):
    return Part(
        part_type=part_type,
        arrival_time_interval=INTERVALS.get(part_type),
        delay_percentage=DELAY_PERCENTAGE.get(part_type)
    )

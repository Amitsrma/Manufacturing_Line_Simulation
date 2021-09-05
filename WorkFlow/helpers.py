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
    # TODO identify if synchronous/asynchronous solution would suffice here
    raise NotImplementedError

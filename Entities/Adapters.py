from collections import deque
from Entities.Part import Part
from Entities.ConveyorLine import Line


class LinePartReleaseQueue(Part, Line):
    """
    Keeps track of which part arrived first in a line
    """
    def __init__(self):
        self.fifo_part_queue = deque()

    def add_part(self, part_to_add: Part) -> None:
        self.fifo_part_queue.append(part_to_add)

    def get_part(self) -> Part:
        return self.fifo_part_queue.popleft()

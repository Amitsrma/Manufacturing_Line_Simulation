from collections import deque
from Part import Part
from typing import Tuple


class Line:
    def __init__(self, identifier: str, delay_distribution: Tuple):
        self.identifier = identifier
        self.num_current_parts = 0
        self.parts_queue = deque()
        self.delay_distribution = delay_distribution
    
    def release_part(self) -> Part:
        self.num_current_parts -= 1
        return self.parts_queue.popleft()
    
    def add_part(self, part_to_add: Part) -> None:
        self.num_current_parts += 1
        self.parts_queue.append(part_to_add)

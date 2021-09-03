from collections import deque
from Part import Part


class Line:
    def __init__(self):
        self.num_current_parts = 0
        self.parts_queue = deque()
    
    def release_part(self) -> Part:
        self.num_current_parts -= 1
        return self.parts_queue.popleft()
    
    def add_part(self, part_to_add: Part) -> None:
        self.num_current_parts += 1
        self.parts_queue.append(part_to_add)

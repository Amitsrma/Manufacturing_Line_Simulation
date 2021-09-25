from EntityManagers.PartQueue import PartQueue
from collections import deque
from Entities.Part import Part


class Line:
    def __init__(self, name: str, capacity: int):
        self.__name = name
        self.capacity = capacity  # num of parts it can accomodate
        self.num_current_parts = 0
        self.parts_queue = deque()

    def release_part(self) -> Part:
        self.num_current_parts -= 1
        return self.parts_queue.popleft()

    def add_parts(self, part_queue: PartQueue) -> None:
        """
        Adds part to the conveyor from PartQueue if operation can be done.
        If it is not possible, leaves PartQueue intact

        Parameters:
            part_queue: Object whose entries will be updated as we move on
        """
        while self.num_current_parts < self.capacity:
            self.num_current_parts += 1
            self.parts_queue.append(part_queue.get_part())

    def is_full(self) -> bool:
        return self.num_current_parts < self.capacity

    def __repr__(self) -> str:
        return f"{self.__name}: (current, {self.num_current_parts}),"\
               f"(capacity, {self.capacity})"

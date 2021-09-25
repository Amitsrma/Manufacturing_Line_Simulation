from collections import deque
from Entities.Part import Part
from typing import List, Union


class PartQueue:
    def __init__(self):
        self._parts = deque()
        self.num_parts = 0

    def get_part(self) -> Part:
        if self.num_parts > 0:
            return self._parts.popleft()
        return None

    def add_parts(self, parts: Union[Part, List[Part]]):
        if isinstance(parts, Part):
            self.num_parts += 1
            self._parts.append(parts)
        elif isinstance(parts, list):
            self.num_parts += len(parts)
            self._parts.extend(parts)
        else:
            raise TypeError("expected types to be either Part or List of Part")

    def __repr__(self) -> str:
        return f"{self._parts}"

from collections import deque
from Entities.Part import Part
from typing import List, Union


class PartQueue(deque):
    def get_part(cls) -> Part:
        if cls.__len__() > 0:
            return cls.popleft()
        return None

    def add_parts(cls, parts: Union[Part, List[Part]]):
        if isinstance(parts, Part):
            cls.append(parts)
        elif isinstance(parts, list):
            cls.extend(parts)
        else:
            raise TypeError("expected either Part or List of Part")

from Entities.Part import Part
from typing import Set


class Pallet:
    __existing_pallet_ids = set()

    def __init__(self, id: int):
        if id in self.__existing_pallet_ids:
            raise ValueError("Duplicate pallet id, pallet ids must be unique")
        self.__existing_pallet_ids.add(id)
        self.id = id
        self.is_free = True
        self.assigned_part = None

    def assign_part(self, assigned_part: Part) -> None:
        self.assigned_part = assigned_part

    def get_used_pallet_ids(self) -> Set:
        return self.__existing_pallet_ids

    def __repr__(self) -> str:
        return f"Pallet: {self.id}"

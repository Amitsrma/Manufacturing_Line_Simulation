from data_store import SPACE_CAP
from Entities.Pallet import Pallet


class Space:
    def __init__(self, id: int):
        self.__id = id
        self.pallets_waiting = []

    def can_pallet_enter(self) -> bool:
        # returns true if space can accomodate a part, else false
        if len(self.parts_waiting) < SPACE_CAP:
            return True
        return False

    def place_pallet(self, a_pallet: Pallet) -> Pallet:
        self.pallets_waiting.append(a_pallet)


class SpaceManager:
    def __init__(self, num_gaps: int):
        self.spaces = [Space(id=index) for index in range(num_gaps)]

    def can_part_enter(self, id: int):
        return self.spaces[id].can_pallet_enter()

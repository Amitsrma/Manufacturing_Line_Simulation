from Entities.Part import Part
from collections import deque
from Entities.Pallet import Pallet


class PalletManager:
    """
    Singleton class:: Keeps track of pallets and their state in the system
    """
    def __init__(self, total_pallets: int):
        self.total_pallets = total_pallets
        self.num_free_pallets = 0
        self.free_pallet_queue = deque([Pallet(i) for i in range(total_pallets)])
        self.used_pallets = deque()

    def get_an_available_pallet(self) -> Pallet:
        self.num_free_pallets -= 1
        return self.free_pallet_queue.popleft()

    def add_to_free_pallet_queue(self, free_pallet: Pallet) -> None:
        self.num_free_pallets += 1
        self.free_pallet_queue.append(free_pallet)

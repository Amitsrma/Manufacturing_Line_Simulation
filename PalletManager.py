from collections import deque
from Pallet import Pallet


class PalletManager:
    def __init__(self, total_pallets: int):
        self.total_pallets = total_pallets
        self.free_pallets = 0
        self.free_pallet_queue = deque()

    def get_an_available_pallet(self) -> Pallet:
        return self.free_pallet_queue.popleft()

    def add_to_free_pallet_queue(self, free_pallet: Pallet) -> None:
        self.free_pallet_queue.append(free_pallet)

from Entities.WorkCell import Workcell
from EntityManagers.PalletManager import PalletManager


class TheSystem:
    def __init__(self, num_workcells: int, num_pallets: int):
        self.workcells = [Workcell(i) for i in range(1, num_workcells+1)]
        self.pallet_manager = PalletManager(total_pallets=num_pallets)

    def can_part_enter(self):
        if not self.workcells[7].is_processing:
            return True
        return False

    def update(self, current_time: int) -> None:
        """
        Updates:
            State of TheSystem for given time.
            Time and processing state of workcell.
            PalletManager's state in the system.
            Space available in between the workcells.
        """
        raise NotImplementedError

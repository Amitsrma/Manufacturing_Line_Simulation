from EntityManagers.WorkCellManager import WorkCellManager
from Entities.BetweenWorkcell import Space
from EntityManagers.PalletManager import PalletManager


class TheSystem:
    def __init__(self, num_workcells: int, num_pallets: int):
        self.workcell_manager = WorkCellManager(num_workcells=num_workcells)
        self.pallet_manager = PalletManager(total_pallets=num_pallets)
        # Add Space Manager

    def can_part_enter(self):
        return self.workcell_manager.can_part_enter(cell_id=7)

    def update(self, current_time: int) -> None:
        """
        Updates:
            State of TheSystem for given time.
            Time and processing state of workcell.
            PalletManager's state in the system.
            Space available in between the workcells.
        """
        # TODO conveyor is always on with current implementation
        raise NotImplementedError("Update system state!")

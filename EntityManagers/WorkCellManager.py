from Entities.WorkCell import Workcell


class WorkCellManager:
    def __init__(self, num_workcells: int):
        self.workcells = [Workcell(i) for i in range(1, num_workcells + 1)]
        self._num_workcells = num_workcells

    def update_cell_states(self) -> None:
        raise NotImplementedError("WorkCellManager update_cell_status()")

    def can_part_enter(self, cell_id: int) -> bool:
        if cell_id < 0 or self._num_workcells < cell_id:
            raise ValueError("cell_id does not exist!")
        return not self.workcells[cell_id].is_processing

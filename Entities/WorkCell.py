from data_store import (
    MANUAL_WORKCELL_SETUP_TIMES, WORKCELL_SETUP_TIMES,
    MANUAL_CELLS)
from Entities.Part import Part


class Workcell:
    def __init__(self, cell_number: int):
        self.cell_number = cell_number
        self.current_part = None
        if self.cell_number in MANUAL_CELLS:
            self.time_to_switch = MANUAL_WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = True
        else:
            self.time_to_switch = WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = False
        self.is_processing = False

    def enter_part(self, part: Part) -> None:
        pass

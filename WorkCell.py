from data_store import (
    MANUAL_WORKCELL_SETUP_TIMES, WORKCELL_SETUP_TIMES,
    MANUAL_CELLS)


class Workcell:
    def __init__(self, cell_number: int):
        self.cell_number = cell_number
        if self.cell_number in MANUAL_CELLS:
            self.time_to_switch = MANUAL_WORKCELL_SETUP_TIMES.get(cell_number)
        else:
            self.time_to_switch = WORKCELL_SETUP_TIMES.get(cell_number)

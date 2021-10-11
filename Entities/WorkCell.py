from data_store import (
    MANUAL_WORKCELL_SETUP_TIMES, WORKCELL_SETUP_TIMES,
    MANUAL_CELLS)
from Entities.Part import Part


class Workcell:
    def __init__(self, cell_number: int):
        self.cell_number = cell_number
        self.most_recent_part = None
        self.part_enter_time = 0
        self.processing_delta = 0
        self.incoming_part = None
        if self.cell_number in MANUAL_CELLS:
            self.time_to_switch = MANUAL_WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = True
        else:
            self.time_to_switch = WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = False
        self.is_processing = False

    def enter_part(self, part: Part, current_time: int) -> bool:
        pass

    def update(self, current_time: int) -> None:
        raise NotImplementedError

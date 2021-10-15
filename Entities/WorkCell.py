from data_store import (
    MANUAL_WORKCELL_SETUP_TIMES, WORKCELL_SETUP_TIMES,
    MANUAL_CELLS)
from Entities.Pallet import Pallet


class Workcell:
    def __init__(self, cell_number: int):
        self.cell_number = cell_number
        self.is_empty = True
        self.is_processing = False
        self.is_setting_up = False
        self.most_recent_part = None
        self.part_enter_time = 0
        self.pallet = None
        self.processing_delta = 0
        self.incoming_part = None
        if self.cell_number in MANUAL_CELLS:
            self.time_to_switch = MANUAL_WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = True
        else:
            self.time_to_switch = WORKCELL_SETUP_TIMES.get(cell_number)
            self.is_manual = False

    def enter_pallet(self, pallet: Pallet, current_time: int) -> bool:
        self.pallet = pallet
        self.part_enter_time = current_time
        if self.most_recent_part != pallet.current_part:
            self.processing_delta = self.time_to_switch.get(pallet.current_part)
            self.is_setting_up = True
        else:
            self.processing_delta = 0
            self.is_setting_up = False

    def update(self, current_time: int) -> None:
        if self.is_setting_up:
            self.processing_delta -= 1

        raise NotImplementedError("Workcell Instance")

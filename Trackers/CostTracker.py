from Entities.Part import Part
from typing import List


class LostCost:
    def __init__(self):
        self.total_cost = 0

    def update_lost_part(self, parts_list: List[Part]) -> None:
        for part in parts_list:
            self.total_cost += part.lost_cost_per_unit

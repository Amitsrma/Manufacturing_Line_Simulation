from Entities.Part import Part


class LostCost:
    def __init__(self):
        self.total_cost = 0

    def update_lost_part(self, part: Part) -> None:
        self.total_cost += part.lost_cost_per_unit

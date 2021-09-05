from data_store import LOST_COST_OF_PART


class Part:
    def __init__(self, part_type: str, arrival_time_interval: int,
            delay_percentage: float) -> None:
        self.part_type = part_type  # A or B or C
        self.arrival_time_interval = arrival_time_interval
        self.delay_percentage = delay_percentage
        self.is_lost = False
        self.lost_cost_per_unit = LOST_COST_OF_PART.get(part_type)

    def __repr__(self) -> str:
        return self.part_type

    def __eq__(self, other_part: 'Part') -> bool:
        return self.part_type == other_part.part_type

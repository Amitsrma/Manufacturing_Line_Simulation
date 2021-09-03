class Part:
    def __init__(self,
            part_type: str,
            arrival_time_interval: int,
            delay_percentage: float
            ) -> None:
        self.part_type = part_type
        self.arrival_time_interval = arrival_time_interval
        self.delay_percentage = delay_percentage
        self.is_lost = False

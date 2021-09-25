from Entities.WorkCell import Workcell


class WorkCellManager:
    def __init__(self, num_workcells: int):
        self.workcells = [Workcell(i) for i in range(1, num_workcells+1)]

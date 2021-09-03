from Part import Part


class Pallet:
    def __init__(self):
        self.is_free = True
        self.assigned_part = None
    
    def assign_part(self, assigned_part: Part) -> None:
        self.assigned_part = assigned_part

from Adapters.PalletAndManagerAdapter import PalletManagerAdapter
from Entities.WorkCell import Workcell


class TheSystem:
    def __init__(self, num_workcells: int, num_pallets: int):
        self.workcells = [Workcell(i) for i in range(1, num_workcells+1)]
        self.pallet_manager = PalletManagerAdapter(total_pallets=num_pallets)

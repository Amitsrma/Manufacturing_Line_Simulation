from Entities.Pallet import Pallet
from EntityManagers.PalletManager import PalletManager


class PalletManagerAdapter(PalletManager, Pallet):
    def __init__(self, total_pallets: int):
        super().init(total_pallets)

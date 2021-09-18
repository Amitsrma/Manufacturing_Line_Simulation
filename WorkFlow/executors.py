from data_store import INTERVALS
from Entities.Part import Part
from EntityManagers import PalletManager, PartGenerators, WorkSystem
from Trackers.CostTracker import LostCost


def run_system(duration: int = 1, num_workcells: int = 8,
               total_pallets: int = 40):
    """
    Executes the logic of system, saves the state of system as is for
    further operation.

    params:
        duration (int): This the number of weeks system is supposed to run
                        continuously

    returns: None
    """
    raise NotImplementedError
    duration_in_seconds = duration * 5 * 16 * 3600  # convert duration to sec
    part_generator = PartGenerators(
        interval_A=INTERVALS.get("A"),
        interval_B=INTERVALS.get("B"),
        interval_C=INTERVALS.get("C")
    )
    cost = LostCost()
    system = WorkSystem(num_workcells=num_workcells, num_pallets=total_pallets)
    while duration_in_seconds >= 0:

        duration_in_seconds -= 1

from data_store import INTERVALS
from Entities.Part import Part
from Entities.ConveyorLine import Line
from EntityManagers.PartGenerators import PartGenerators
from EntityManagers.PartQueue import PartQueue, PartQueues
from Trackers.CostTracker import LostCost
from WorkFlow.helpers import get_part, initialize


def run_system(duration: int = 1, num_workcells: int = 8,
               total_pallets: int = 40,
               input_conveyor_cap: int = 40):
    """
    Executes the logic of system, saves the state of system as is for
    further operation.

    params:
        duration (int): This the number of weeks system is supposed to run
                        continuously

    returns: None
    """
    initialize()
    duration_in_seconds = duration * 5 * 16 * 3600  # convert duration to sec
    part_generator = PartGenerators(
        part_A=get_part("A"),
        part_B=get_part("B"),
        part_C=get_part("C")
        )
    cost = LostCost()
    system = WorkSystem(num_workcells=num_workcells, num_pallets=total_pallets)
    input_line = Line(name="Input Conveyor", capacity=input_conveyor_cap)
    queue_to_input_line = PartQueue()

    while duration_in_seconds >= 0:
        if not input_line.is_full():
            generated_parts = part_generator.get_parts()
            queue_to_input_line.add_parts(generated_parts)
            input_line.add_parts(part_queue=queue_to_input_line)
        # if input_line is full, stop part generation until space is available

        duration_in_seconds -= 1
        raise NotImplementedError

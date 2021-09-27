from data_store import INTERVALS
from Entities.Part import Part
from Entities.ConveyorLine import Line
from EntityManagers.WorkSystem import TheSystem
from EntityManagers.PartGenerators import PartGenerator
from EntityManagers.PartQueue import PartQueue
from Trackers.CostTracker import LostCost
from WorkFlow.helpers import get_part


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
    duration_in_seconds = duration * 5 * 16 * 3600  # convert duration to sec
    part_generator = PartGenerator(
        part_A=get_part("A"),
        part_B=get_part("B"),
        part_C=get_part("C")
        )
    cost = LostCost()
    system = TheSystem(num_workcells=num_workcells, num_pallets=total_pallets)
    input_line = Line(name="Input Conveyor", capacity=input_conveyor_cap)
    queue_to_input_line = PartQueue()

    while duration_in_seconds >= 0:
        generated_parts = part_generator.get_parts(duration_in_seconds)
        # Log generated parts
        if not input_line.is_full():
            queue_to_input_line.add_parts(generated_parts)
            input_line.add_parts(part_queue=queue_to_input_line)
        # if input_line is full, stop part generation until space is available
        else:
            # Log lost parts
            cost.update_lost_part(generated_parts)
            # Log lost cost to this point in time
        if system.can_part_enter():
            raise NotImplementedError("TheSystem logics to be added!")
        duration_in_seconds -= 1
        raise NotImplementedError


if __name__ == "__main__":
    run_system(
        duration=1,
        num_workcells=8,
        total_pallets=40,
        input_conveyor_cap=40
    )

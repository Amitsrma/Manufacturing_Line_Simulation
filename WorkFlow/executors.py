from logging import Logger
from data_store import INTERVALS
from Entities.Part import Part
from Entities.ConveyorLine import Line
from EntityManagers.WorkSystem import TheSystem
from EntityManagers.PartGenerators import PartGenerator
from EntityManagers.PartQueue import PartQueue
from event_logger import LOGGER
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

    current_time = 0
    while current_time < duration_in_seconds:
        generated_parts = part_generator.get_parts(duration_in_seconds)
        if len(generated_parts) > 0:
            LOGGER.info(f"{current_time}: Parts Generated - {generated_parts}")
        if not input_line.is_full():
            queue_to_input_line.add_parts(generated_parts)
            input_line.add_parts(part_queue=queue_to_input_line)
        # if input_line is full, stop part generation until space is available
        else:
            LOGGER.info(f"{current_time}: Lost Parts - {generated_parts}")
            cost.update_lost_part(generated_parts)
            LOGGER.info(f"Lost Cost: {cost.total_cost}")
        if system.can_part_enter():
            raise NotImplementedError("TheSystem logics to be added!")
        current_time += 1
        raise NotImplementedError


if __name__ == "__main__":
    run_system(
        duration=1,
        num_workcells=8,
        total_pallets=40,
        input_conveyor_cap=40
    )

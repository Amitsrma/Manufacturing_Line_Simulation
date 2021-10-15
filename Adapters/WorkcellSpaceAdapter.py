"""
[7] SP6 [6] SP5 [5]

SP7             SP4

[8]             [4]

SP8             SP3

[1] SP1 [2] SP2 [3]

Adapter to capture the interaction of WorkCell (represented as Square Brackets)
and Space between WorkCells (represented as SPi above). Numbers in square
brackets refer to the WorkCell number.
This will capture interaction between WorkCell_i and SPi, SPi-1
"""
from Entities.WorkCell import Workcell
from Entities.BetweenWorkcell import Space
from Entities.BetweenWorkcell import SpaceManager


# TODO find out if Space or SpaceManager is better used here
# Space alone won't allow sharing same Space over multiple cells
# if we use one Adapter per Workcell
class WorkcellSpaceAdapter(Space, Workcell):
    def __init__(self, cell_number: int, space_manager: SpaceManager):
        Workcell.__init__(self, cell_number)

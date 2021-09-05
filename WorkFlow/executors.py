from Entities.Part import Part
from EntityManagers import PalletManager


def run_system(duration: int = 1):
    """
    Executes the logic of system, saves the state of system as it 

    params:
        duration (int): This the number of weeks system is supposed to run
                        continuously

    returns: None
    """
    duration_in_seconds = duration * 5 * 16 * 3600  # convert duration to sec
    while duration_in_seconds >= 0:
        
        duration_in_seconds -= 1
    raise NotImplementedError

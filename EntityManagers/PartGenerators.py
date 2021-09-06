from Entities.Part import Part
from data_store import ALLOWED_KEYS


class PartGenerator:
    """
    Singleton Class
    This will resemble Line A, Line B and Line C
    At any instance, it will mention if part A, B or C will be generated.
    Allowed Keys for the kwargs so far are:
        interval_A, interval_B, interval_C
    """
    def __init__(self, **kwargs):
        allowed_arguments = {key: value for key, value in kwargs.items()}
        self.__dict__.update(allowed_arguments)

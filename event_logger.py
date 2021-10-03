import logging
import logging.handlers


LOG_FILE_NAME = "event_logs"
LOGGER_NAME = "EVENT_LOG"


def create_logger():
    log = logging.getLogger(LOGGER_NAME)
    log.setLevel(logging.INFO)
    rotating_fhandler = logging.handlers.RotatingFileHandler(
        filename=LOG_FILE_NAME
    )
    formatter = logging.Formatter("%(name)s - %(levelname)s : %(message)s")
    rotating_fhandler.setFormatter(formatter)
    log.addHandler(rotating_fhandler)
    return log


LOGGER = create_logger()

from pathlib import Path

current_dir = Path(__file__).parent.absolute()
LOG_FILENAME = "operation_log.csv"
LOG_FILEPATH = Path(current_dir, LOG_FILENAME)

PROD_LOG = "operation_log"

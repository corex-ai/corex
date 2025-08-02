import logging

logger = logging.getLogger("corex_logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("corex_logs.log")
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

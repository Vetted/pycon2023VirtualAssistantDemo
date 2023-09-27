import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

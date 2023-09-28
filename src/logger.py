import logging
import sys

# qdrant logger settings
logging.getLogger("quart.serving").setLevel(logging.ERROR)

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

import arqLogger

# create new logger
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# add a rotating handler
handler = RotatingFileHandler("log_file.log", maxBytes=1000000, backupCount=5)
logger.addHandler(handler)


def on_new_log(log):
    logger.info("%s - %s" % (datetime.now(), log))


arqLogger.start_websocket(3000, on_new_log)

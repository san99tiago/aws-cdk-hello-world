# Built-in imports
import os
import logging
from datetime import datetime


# Configure logging
loglevel = logging.getLevelName(os.environ.get("LOG_LEVEL", "INFO").upper())
LOGGER = logging.getLogger()
LOGGER.setLevel(loglevel)


def lambda_handler(event, context):
    LOGGER.info("lambda_handler: EVENT is {}".format(event))
    LOGGER.debug("lambda_handler: CONTEXT is {}".format(context))

    current_utc_time = datetime.now().strftime("%Y_%m_%d-%H_%M_%SZ")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {
            "datetime": current_utc_time,
            "message": "Hello from Santi",
            "note": "I wish that you have an excellent day",
        }
    }

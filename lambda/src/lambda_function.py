# Built-in imports
from datetime import datetime
import boto3


def get_current_aws_account():
    """
    Simple usage of boto3 to get current AWS account
    """
    client = boto3.client("sts")
    return client.get_caller_identity()["Account"]


def lambda_handler(event, context):
    # print("lambda_handler: <event> is {}".format(event))

    current_utc_time = datetime.now().strftime("%Y_%m_%d-%H_%M_%SZ")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {
            "account": get_current_aws_account(),
            "datetime": current_utc_time,
            "message": "Hello from Santi",
        }
    }

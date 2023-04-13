import os

from aws_cdk import (
    Stack,
    Duration,
    aws_lambda,
)
from constructs import Construct

class CdkHelloWorldStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Get relative path for folder that contains Lambda function sources
        # ! Note--> we must obtain parent dirs to create path (that's why there is "os.path.dirname()")
        top_level_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        PATH_TO_FUNCTION_FOLDER = os.path.join(
            top_level_path,
            "lambda",
            "src",
        )
        print("Source code for lambda function obtained from: ", PATH_TO_FUNCTION_FOLDER)

        self.simple_lambda = aws_lambda.Function(
            self,
            id="{}Lambda".format(construct_id),
            function_name="hello-world-lambda-function",
            description="Simple hello world function deployed with AWS CDK",
            code=aws_lambda.Code.from_asset(PATH_TO_FUNCTION_FOLDER),
            handler="lambda_function.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            timeout=Duration.seconds(5),
            memory_size=128,
            environment={"LOG_LEVEL": "DEBUG"},  # "INFO" or "DEBUG" (based on log_level requirements)
        )

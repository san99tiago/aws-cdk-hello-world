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
        PATH_TO_FUNCTION_FOLDER = os.path.join(
            os.path.dirname(__file__),
            "lambda"
        )
        print("Source code for lambda function obtained from: ", PATH_TO_FUNCTION_FOLDER)

        self.simple_lambda = aws_lambda.Function(
            self,
            id="{}Lambda".format(construct_id),
            function_name="HelloWorldLambdaFunction",
            description="Simple Hello-World function deployed with AWS CDK",
            code=aws_lambda.Code.from_asset(PATH_TO_FUNCTION_FOLDER),
            handler="lambda_function.lambda_handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            timeout=Duration.seconds(10),
            memory_size=128,
        )
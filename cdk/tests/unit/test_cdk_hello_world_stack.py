import aws_cdk as core
import aws_cdk.assertions as assertions

from stacks.cdk_hello_world_stack import CdkHelloWorldStack


app = core.App()
stack = CdkHelloWorldStack(app, "cdk-hello-world")
template = assertions.Template.from_stack(stack)


def test_iam_role_for_lambda_created():
    template.has_resource_properties(
        "AWS::IAM::Role",
        {
            "AssumeRolePolicyDocument": {
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "lambda.amazonaws.com"
                        }
                    }
                ],
            }
        }
    )


def test_lambda_function_created():
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {
            "Handler": "lambda_function.lambda_handler",
            "Runtime": "python3.9",
            "FunctionName": "hello-world-lambda-function",
        }
    )

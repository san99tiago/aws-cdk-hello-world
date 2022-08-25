import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_hello_world.cdk_hello_world_stack import CdkHelloWorldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_hello_world/cdk_hello_world_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkHelloWorldStack(app, "cdk-hello-world")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lambda_devcontainer.cdk_lambda_devcontainer_stack import CdkLambdaDevcontainerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lambda_devcontainer/cdk_lambda_devcontainer_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLambdaDevcontainerStack(app, "cdk-lambda-devcontainer")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

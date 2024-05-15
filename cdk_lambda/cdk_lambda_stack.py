from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_iam,
)
from constructs import Construct

class CdkLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # permissions for s3 for Lambda Function
        perm_statement_s3 = aws_iam.PolicyStatement()
        perm_statement_s3.add_actions(
            "s3:*",
        )
        perm_statement_s3.add_resources("*")

        #creates the lambda function for dynamodb put
        lambda_Fn = aws_lambda.Function(
            self, 
            "cdklambda",
            code=aws_lambda.AssetCode('lambda_funct'),
            runtime=aws_lambda.Runtime.PYTHON_3_11,
            handler='lambda_function.lambda_handler',
            memory_size=512,
            timeout=Duration.seconds(120), 
            environment={
            },
        )

        lambda_Fn.add_to_role_policy(perm_statement_s3)
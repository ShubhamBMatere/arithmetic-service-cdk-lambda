from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
)
from constructs import Construct

class ArithmeticCalServiceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        arithmetic_lambda = _lambda.Function(
            self, 'ArithmeticLambda',
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler='arithmetic_service.handler',
            code=_lambda.Code.from_asset('lambda'),
        )

        # Define API Gateway
        api = apigateway.LambdaRestApi(
            self, 'ArithmeticAPI',
            handler=arithmetic_lambda,
            proxy=False
        )

        # Define the 'v1' resource once
        v1_resource = api.root.add_resource('v1')

        # Add arithmetic operation resources under 'v1'
        add_resource = v1_resource.add_resource('add')
        subtract_resource = v1_resource.add_resource('subtract')
        multiply_resource = v1_resource.add_resource('multiply')
        divide_resource = v1_resource.add_resource('divide')

        # Define HTTP methods for each resource
        add_resource.add_method('GET')
        subtract_resource.add_method('GET')
        multiply_resource.add_method('GET')
        divide_resource.add_method('GET')

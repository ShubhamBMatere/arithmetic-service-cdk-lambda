import aws_cdk as core
import aws_cdk.assertions as assertions

from deqode_persi.deqode_persi_stack import DeqodePersiStack

# example tests. To run these tests, uncomment this file along with the example
# resource in deqode_persi/deqode_persi_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DeqodePersiStack(app, "deqode-persi")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

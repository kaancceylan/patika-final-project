import aws_cdk as core
import aws_cdk.assertions as assertions

from patika_final_hw.vpc_stack import PatikaFinalHwStack

# example tests. To run these tests, uncomment this file along with the example
# resource in patika_final_hw/patika_final_hw_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PatikaFinalHwStack(app, "patika-final-hw")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class VPCStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        self.vpc = ec2.Vpc(self, "PatikaVPC", 
                            max_azs=1, #Max number of availability zones
                            cidr="10.0.0.0/16", #10.0 for network, 0.0 for hosts, 65536 host IP 
                            subnet_configuration=[
                                ec2.SubnetConfiguration(
                                    subnet_type=ec2.SubnetType.PUBLIC,
                                    #Has internet access (route table has internet gateway listed)
                                    name="PatikaPublicSub",
                                    cidr_mask=24 # 10.0.0.0/24
                                ), 
                                ec2.SubnetConfiguration(
                                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                                    #Does not have internet access, needs NAT on public subnet 
                                    name="PatikaPrivateSub",
                                    cidr_mask=24 # 10.0.1.0/24
                                )
                            ],
                        )
#!/usr/bin/env python3
import os
import aws_cdk as cdk

from patika_final_hw.vpc_stack import VPCStack
from patika_final_hw.cdn_stack import CDNStack

app = cdk.App()

# PCStack instance. Deploy the VPC Stack with 1 public and 1 private subnet
VPCStack(app, "VPCStack",
        env=cdk.Environment(account="177836715603", region="eu-central-1"),
        )

# CDNStack instance. Deploy the CDN Stack with an asset bucket, OIA and Cloudfront origin
CDNStack(app, "S3Stack",
        env=cdk.Environment(account='177836715603', region='eu-central-1'),
        )

app.synth()

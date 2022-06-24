from aws_cdk import (
    RemovalPolicy,
    Stack,
    CfnOutput,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as cloudfront_origin
)

from constructs import Construct

class CDNStack(Stack):


    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        s3_origin_bucket = s3.Bucket(self, "PatikaCDNBucket",
                            bucket_name="patika-cdn-bucket",
                            block_public_access=s3.BlockPublicAccess.BLOCK_ALL, # Only cloudfront will have access to the assets.
                                    )
                                    # Do not set the removal policy to destroy, can break your CDK stack.

        CfnOutput(self, "CDNBucketEnvARN",
                export_name="CDNBucketEnvARN",
                value=s3_origin_bucket.bucket_arn)

        CfnOutput(self, "CDNBucketEnv",
                export_name="CDNBucketEnv",
                value=s3_origin_bucket.bucket_name)

        my_cdn_dist = cloudfront.CloudFrontWebDistribution(self, 'PatikaCDNStack', 
                                                                    origin_configs=[cloudfront.SourceConfiguration(
                                                                        s3_origin_source=cloudfront.S3OriginConfig(
                                                                            s3_bucket_source=s3_origin_bucket,
                                                                            origin_access_identity= cloudfront.OriginAccessIdentity(self, 'OriginAccessIdentity',
                                                                            comment='OriginAccessIdentity for patika-cdn-bucket')
                                                                        ),
                                                                        behaviors=[cloudfront.Behavior(is_default_behavior=True)]
                                                                        #default behavior sets things like cache behavior, minTTL, maxTTL etc.
                                                                    )
                                                                    ])
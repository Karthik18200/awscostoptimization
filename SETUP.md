# Setup Instructions

1. Create an IAM role using iam_policy.json.
2. Create a Lambda function in AWS.
3. Upload lambda_function.py as the handler.
4. Attach IAM role to Lambda.
5. Create a CloudWatch rule using cloudwatch_rule.json to trigger daily.
6. Test the function and monitor logs in CloudWatch.

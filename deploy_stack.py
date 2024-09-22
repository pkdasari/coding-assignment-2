import boto3
import sys

def create_stack_set(customer_name, archive_acc_id, customer_acc_id, bucket_name):
    # Initialize a CloudFormation client
    client = boto3.client('cloudformation')

    # Define the StackSet name and parameters
    stack_name = f"{customer_name}-event-logging-stack"
    template_body = open('./event_logging_stack.yaml').read()

    # Parameters for the stack
    parameters = [
        {
            'ParameterKey': 'CustomerAccountId',
            'ParameterValue': customer_acc_id
        },
        {
            'ParameterKey': 'ArchiveAccountId',
            'ParameterValue': archive_acc_id
        },
        {
            'ParameterKey': 'BucketName',
            'ParameterValue': bucket_name
        },
        {
            'ParameterKey': 'LambdaFunctionName',
            'ParameterValue': f"{customer_name}-login-logger"
        }
    ]

    try:
        response = client.create_stack_set(
            StackSetName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters,
            Capabilities=['CAPABILITY_NAMED_IAM'],
            AdministrationRoleARN='arn:aws:iam::<your-admin-account-id>:role/<your-admin-role>',  # Replace with your admin role
            ExecutionRoleName='<your-execution-role>'  # Replace with your execution role
        )
        print(f"StackSet created successfully: {response['StackSetId']}")
    except Exception as e:
        print(f"Failed to create StackSet: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python deploy_stack.py <customer_name> <archive_acc_id> <customer_acc_id> <bucket_name>")
        sys.exit(1)

    customer_name = sys.argv[1]
    archive_acc_id = sys.argv[2]
    customer_acc_id = sys.argv[3]
    bucket_name = sys.argv[4]

    create_stack_set(customer_name, archive_acc_id, customer_acc_id, bucket_name)

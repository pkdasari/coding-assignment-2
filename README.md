
# Centralized Event Logging Automation

This project automates the deployment of a Lambda function in newly created AWS accounts to centralize event logging. The function captures user login events and stores them as JSON files in an S3 bucket located in a designated shared account.

### Prerequisites

Make sure to have the AWS CLI installed and configured with the necessary permissions to deploy CloudFormation stacks and create resources.

* Python: Ensure you have Python 3.x installed. You can download it from python.org.

* Pip: Ensure you have pip installed for package management. It usually comes bundled with Python installations. You can check if it's installed by running:

```bash
pip --version
```

* AWS CLI: Install the AWS CLI and configure it with the necessary credentials. Instructions can be found here.

* Boto3 Library: This Python library is used to interact with AWS services. Install it using pip:

```bash
pip install -r requirements.txt
```

## CloudFormation Template

The CloudFormation template (`event_logging_stack.yaml`) defines:
- A Lambda function to log user login events.
- An IAM role with permissions to write logs to the S3 bucket.
- Parameterization to customize resource deployment for each new account.

## Scripts

### Python Script

Run the Script: Execute the script with the required parameters:

```bash
python3 scripts/deploy_stack.py <customer_name> <archive_acc_id> <customer_acc_id> <bucket_name>
```

### Example Invocation
To deploy the Lambda function for a new customer account, run:

```bash
python deploy_stack.py customer1 123456789012 987654321098 my-log-bucket
```

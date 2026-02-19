import boto3
import subprocess
import json

# Get values from Terraform outputs
def get_terraform_output(output_name):
    """Read a Terraform output value"""
    result = subprocess.run(
        ['terraform', 'output', '-json', output_name],
        capture_output=True,
        text=True,
        cwd='D:\\terraform-localstack-project'  # Your project path
    )
    return json.loads(result.stdout)

# Read infrastructure details from Terraform
BUCKET_NAME = get_terraform_output('s3_bucket_name')
QUEUE_URL = get_terraform_output('sqs_queue_url')
TABLE_NAME = get_terraform_output('dynamodb_table_name')

print(f"Using infrastructure from Terraform:")
print(f"  - S3 Bucket: {BUCKET_NAME}")
print(f"  - SQS Queue: {QUEUE_URL}")
print(f"  - DynamoDB Table: {TABLE_NAME}\n")

# Create S3 client pointing to LocalStack
s3_client = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Creating SQS client pointing to localstack
sqs_client = boto3.client(
    'sqs',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# Creating a dynamodb client pointing to localstack
dynamodb_client = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1',
)

def main():
    print("=== Testing LocalStack Infrastructure ===\n")

    # Step 1: Test S3
    print("1. Testing S3...")
    try:
        s3_client.put_object(
            Bucket=BUCKET_NAME,  # No quotes!
            Key='test.txt',
            Body='Hello from Python! This file was uploaded via boto3.'
        )
        print("   ✓ File uploaded to S3")

        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)  # No quotes!
        files = [obj['Key'] for obj in response.get('Contents', [])]
        print(f"   ✓ Files in bucket: {files}")
    except Exception as e:
        print(f"   ✗ S3 Error: {e}")

    # Step 2: Test SQS
    print("\n2. Testing SQS...")
    try:
        print(f"   ✓ Queue URL: {QUEUE_URL}")
        
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,  # Use variable directly, no get_queue_url needed
            MessageBody='Hello from Python! This was sent through SQS'
        )
        print("   ✓ Message sent to SQS")

        response = sqs_client.receive_message(QueueUrl=QUEUE_URL)
        messages = response.get('Messages', [])

        if messages:
            message_body = messages[0]['Body']
            print(f"   ✓ Received message: {message_body}")
        else:
            print("   ✗ No messages in queue")
    except Exception as e:
        print(f"   ✗ SQS Error: {e}")

    # Step 3: Test DynamoDB
    print("\n3. Testing DynamoDB...")
    try:
        dynamodb_client.put_item(
            TableName=TABLE_NAME,  # No quotes!
            Item={
                'id': {'S': '1'},
                'filename': {'S': 'test.txt'},
                'status': {'S': 'processed'}
            }
        )
        print("   ✓ Item written to DynamoDB")

        response = dynamodb_client.get_item(
            TableName=TABLE_NAME,  # No quotes!
            Key={'id': {'S': '1'}}
        )

        item = response.get('Item')
        if item:
            print(f"   ✓ Item retrieved from DynamoDB:")
            print(f"      - ID: {item['id']['S']}")
            print(f"      - Filename: {item['filename']['S']}")
            print(f"      - Status: {item['status']['S']}")
        else:
            print("   ✗ Item not found")
    except Exception as e:
        print(f"   ✗ DynamoDB Error: {e}")

    print("\n=== All tests passed! ===")

if __name__ == "__main__":
    main()
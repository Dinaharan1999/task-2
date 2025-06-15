import boto3
from botocore.exceptions import ClientError

def create_iam_user(username, policy_arn="arn:aws:iam::aws:policy/ReadOnlyAccess"):
    iam = boto3.client('iam')

    try:
        # Step 1: Create IAM user
        iam.create_user(UserName=username)
        print(f"IAM user '{username}' created successfully.")

        # Step 2: Attach managed policy (ReadOnlyAccess by default)
        iam.attach_user_policy(
            UserName=username,
            PolicyArn=policy_arn
        )
        print(f"Policy '{policy_arn}' attached to user '{username}'.")

        # Optional: Create access key
        # key_response = iam.create_access_key(UserName=username)
        # print("Access Key ID:", key_response['AccessKey']['AccessKeyId'])
        # print("Secret Access Key:", key_response['AccessKey']['SecretAccessKey'])

    except ClientError as e:
        error_message = e.response['Error']['Message']
        print(f"Error: {error_message}")

# ----------- MAIN BLOCK ------------
if __name__ == "__main__":
    # Take username as input at the end of the code
    username = input("Enter the IAM username to create: ")
    create_iam_user(username)

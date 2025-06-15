### IAM User Creation Script with Python
This Python script automates the creation of an AWS IAM user and attaches a managed policy (ReadOnlyAccess by default) using the boto3 library.

### Features
- Creates a new IAM user
- Attaches the AWS-managed ReadOnlyAccess policy
- Accepts the IAM username dynamically via user input
- Clean and modular structure
- (Optional) Includes support for creating access keys (commented out)


### Prerequisites
- Python 3.6 or above
- AWS account with IAM permissions to create users and attach policies
- Install the required library:
`pip install boto3`

### How to Use
- Save the script as create_iam_user.py.
- Open your terminal and run the script:

`python create_iam_user.py`

- When prompted, enter the desired IAM username.
`Enter the IAM username to create:`


The script will:

- Create the IAM user
- Attach the ReadOnlyAccess policy
- To also create access keys for the user, uncomment the related lines in the script.


### Example Output

- Enter the IAM username to create: test-user
- IAM user 'test-user' created successfully.
- Policy 'arn:aws:iam::aws:policy/ReadOnlyAccess' attached to user 'test-user'.


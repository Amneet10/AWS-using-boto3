import boto3

# Create an S3 client using boto3
client = boto3.client('s3')

# List all S3 buckets
response = client.list_buckets()
# Print the raw response from the list_buckets call to see its structure
print(response)

# Check if the 'Buckets' key is present in the response
if 'Buckets' in response:
    # If present, assign the list of buckets to dict1
    dict1 = response['Buckets']

# Iterate over each item (bucket dictionary) in the list of buckets
for item in dict1:
    # Check if the 'Name' key exists in the current bucket dictionary
    if 'Name' in item:
        # If present, assign the bucket name to dict2
        dict2 = item['Name']
        # Print the bucket name
        print(dict2)

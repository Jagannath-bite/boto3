import boto3

client = boto3.client('iam',aws_access_key_id = 'AKIAXIYFJPH5VVWXA6WV',
	 	aws_secret_access_key = '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')

response = client.list_users()

print(response['Users'])

for i in response['Users']:
	print(i['UserName'])

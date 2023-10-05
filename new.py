import boto3
import csv
def ec2_fun(witer):

	test_dict= {}

    client = boto3.client('ec2',region_name="ap-south-1",aws_access_key_id="AKIAXIYFJPH5T5OE3M5D",aws_secret_access_key="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")

    response = client.describe_instances()
    print(response['Reservations'])

    for i in response ['Reservations'] :
 	print(i['Instances'])

    for j in i ['Instances']:
    print ("**current values**")
    print (j['InstanceId'], j['InstanceType'], j['LaunchTime'], j['ImageId'])
    print ("*****Started Generating the CSV File******")
    test_dict['Instance_Id'] = j['InstnaceID']
    test_dict['Instance_Type'] = j['InstanceType']
    test_dict['Created_date'] = j['ImageId']
    writer.writerow(test_dict)
    print("*****CSV Generated Successfully")
	 	
def main():
	fieldnames = ["Instance_Id","Instance_Type","Created_date","AMI_ID"]
	file_name = "test_dict.csv"
	with open (file_name, "w",newline='') as csv_file:
	writer.writerheader()
	ec2_fun(writer)

main()

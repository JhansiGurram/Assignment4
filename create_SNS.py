import boto3
import config
import json

client = boto3.client('secretsmanager')



def fetchSecret():
    response = client.get_secret_value(
    SecretId='mysns'
    )
    database_secrets = json.loads(response['SecretString'])
    return database_secrets['Topic']

fetch =  fetchSecret()
print(fetch)

sns_client = boto3.client('sns', region_name='us-east-1')

response = sns_client.create_topic(Name=fetch)

topic_arn = response['TopicArn']

response=sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=config.email_Id
)
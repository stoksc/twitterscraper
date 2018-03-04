''' This module defines functions to connect to a DynamoDB instance.
'''

import boto3
from botocore.exceptions import ClientError

def get_dynamodb_table(table=None, access_key=None, secret_key=None):
    ''' This function takes a table name and key pair and returns a dynamodb
    table. If the table already existed, it returns the existing table.
    Otherwise, it creates a new table.
    '''
    assert access_key and secret_key and table
    dynamodb = get_dynamodb_connection(access_key=access_key,
                                       secret_key=secret_key)
    try:
        hashtag_table = create_table(dynamodb=dynamodb, table=table)
    except ClientError:
        hashtag_table = dynamodb.Table(name=table)
    return hashtag_table


def get_dynamodb_connection(access_key=None, secret_key=None):
    ''' This function takes an AWS key pair and returns a dynamodb connection.
    '''
    assert access_key and secret_key
    return boto3.resource(
        'dynamodb',
        region_name='us-east-2',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )


def create_table(dynamodb=None, table=None):
    ''' This function tries to create a table in the provided dynamodb instance
    with the provided hashtag as its name. Raises and error to the calling
    function if the table already exists.
    '''
    assert dynamodb and table
    return dynamodb.create_table(
        TableName=table,
        AttributeDefinitions=[
            {
                'AttributeName': 'entry_id',
                'AttributeType': 'N',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'entry_id',
                'KeyType': 'HASH',
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

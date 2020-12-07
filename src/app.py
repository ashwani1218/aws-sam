import json
import os
import boto3


print("loading function")

# Creating client outside of the handler
regionName = os.environ["REGION_NAME"]
dynamo = boto3.client('dynamodb', regionName=regionName)
tableName = os.environ['TABLE_NAME']


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    """
    This is a simple function which scan the dynamo DB table we have set in environment variables in template.yaml
    """
    scan_result = dynamo.scan(tableName=tableName)
    return respond(None, res=scan_result)

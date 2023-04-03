import os
import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME'] # get endpoint name
runtime= boto3.client('runtime.sagemaker') # make low level sagemaker client

def lambda_handler(event, context):
    data = json.loads(json.dumps(event)) 
    payload = data['data'] #get data from event param
    print(payload)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
        ContentType='text/csv',
        Body=payload)  #call endpoint with endpoint name, type, and payload
    result = json.loads(response['Body'].read().decode()) # get response
    print(result)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': result
    }
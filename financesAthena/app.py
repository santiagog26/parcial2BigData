import time
import boto3


DATABASE = 'yahoo_finances'
TABLE = 'finances'
S3_OUTPUT = 's3://zappa-parcial2'
S3_BUCKET = 'zappa-parcial2'

def handler(event, context):
    query = 'MSCK REPAIR TABLE `finances`;'
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
        }
    )
    return response
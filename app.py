import json

def handler(event, context):
    print("hello from zappa")
    print(event)
    return {'status': 200}
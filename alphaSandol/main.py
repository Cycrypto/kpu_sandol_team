import json
# from .lambda_module import *
from .resource import *
import base64

def lambda_handler(event, context):
    return_string = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[Main Function Error]" + str("test")
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "도움말",
                    "action": "message",
                    "label": "도움말"
                }
            ]
        }
    }

    return {
        'statusCode': 200,
        'body': json.dumps(return_string),
        'headers': {
            'Access-Control-Allow-Origin': '*',
        }
    }
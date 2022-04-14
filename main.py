import json
import boto3
from flask import Flask

app = Flask(__name__)
lambda_client = boto3.client('lambda', region_name='ap-northeast-2')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/invoke")
def invoke():
    res = lambda_client(
        FunctionName='invoke_lambda',
        Payload=json.dumps({
            'hostname': 'example.com',
            'port': 443,
            'path': '/',
            'method': 'GET'
        }))
    return res

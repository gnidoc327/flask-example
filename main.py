import json
import boto3
from flask import Flask

app = Flask(__name__)
lambda_client = boto3.client("lambda", region_name="ap-northeast-2")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/invoke")
def invoke():
    res = lambda_client.invoke(
        FunctionName="invoke_lambda",
        Payload=json.dumps(
            {
                "options": {
                    "hostname": "example.com",
                    "port": 443,
                    "path": "/",
                    "method": "GET",
                },
                "data": {"message": "ok"},
            }
        ),
    )
    return res.get("Payload").read()

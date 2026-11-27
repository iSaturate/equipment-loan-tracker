import json

# TODO: implement CRUD routes (POST, GET, PUT, DELETE) backed by DynamoDB
def lambda_handler(event, context):
    return {"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": json.dumps({"message": "Equipment Loan Tracker API is alive"})}

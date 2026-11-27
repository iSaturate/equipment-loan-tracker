# Equipment Loan Tracker (Serverless on AWS)

Individual Cloud Computing project - Track C (Serverless) on AWS Learner Lab.

## Use case
A small API to record lab equipment loans: borrow, list, update (for example mark returned) and delete loans.

## Architecture
Client to API Gateway (HTTP API) to Lambda (Python 3.12) to DynamoDB. Lambda runs with LabRole and writes logs to CloudWatch.
Diagram: docs/architecture.png

## Endpoints
- POST /loans - create a loan
- GET /loans - list loans
- PUT /loans/{id} - update a loan
- DELETE /loans/{id} - delete a loan

## Deployment plan
See docs/deployment-plan.md

## Status
Week 12: design and AWS setup in progress.

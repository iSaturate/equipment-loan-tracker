# Deployment plan

1. Create DynamoDB table Loans (partition key loanId, String, on-demand capacity).
2. Create Lambda function loan-handler (Python 3.12) using the existing LabRole.
3. Create an HTTP API in API Gateway with routes POST /loans, GET /loans, PUT /loans/{id}, DELETE /loans/{id} integrated with the Lambda function.
4. Test each route with curl and save the outputs as evidence.
5. Cost control: on-demand DynamoDB, 128 MB Lambda, delete resources after grading.

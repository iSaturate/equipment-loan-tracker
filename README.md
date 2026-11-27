# Equipment Loan Tracker (Containers on AWS)

Individual Cloud Computing project - Track B (EC2 + Docker + ECR), AWS Academy lab.

## Use case
A small API to record lab equipment loans: borrow, list, update (for example mark returned) and delete loans.

## Architecture
Client to an EC2 instance running a Docker container. The image is built from app/Dockerfile and stored in Amazon ECR. Diagram: docs/architecture.png

## Planned endpoints
- POST /loans - create a loan
- GET /loans - list loans
- PUT /loans/{id} - update a loan
- DELETE /loans/{id} - delete a loan

## Deployment plan
See docs/deployment-plan.md

## Status
Week 12: design done, Docker image built locally, EC2 and ECR provisioned and tested.

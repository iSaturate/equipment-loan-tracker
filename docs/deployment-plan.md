# Deployment plan

1. Build the Docker image locally from app/Dockerfile (docker build -t loan-tracker:v1 app).
2. Create a private ECR repository named loan-tracker.
3. Launch one EC2 instance (t3.micro, Amazon Linux) with a security group that allows HTTP on port 80.
4. Install Docker on the instance and run a container, then test connectivity with curl against the public IP.
5. Later: push the image to ECR, pull and run it on EC2, and implement the four CRUD endpoints.
6. Cost control: one small instance, terminate it after testing.

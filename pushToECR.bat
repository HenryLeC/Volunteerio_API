aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 729132262671.dkr.ecr.us-east-2.amazonaws.com/volunteerio
docker build -t 729132262671.dkr.ecr.us-east-2.amazonaws.com/volunteerio .
docker push 729132262671.dkr.ecr.us-east-2.amazonaws.com/volunteerio
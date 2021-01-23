#!/bin/bash
scp -i ~/.ssh/id_rsa qa-project2/docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI} 
     
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml qa-project2-v
EOF
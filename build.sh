#!/bin/bash

docker compose down

chmod +x web_start.sh
chmod +x web_start-2.sh
chmod +x web_start-3.sh
chmod +x backend_start.sh

docker rmi greaterwms:backend
docker rmi greaterwms:front
docker rmi greaterwms:front-2
docker rmi greaterwms:front-3

docker build -t greaterwms:backend --target backend .
docker build -t greaterwms:front --target front .
docker build -t greaterwms:front-2 --target front-2 .
docker build -t greaterwms:front-3 --target front-3 .
#!/bin/bash

docker build -t greaterwms:backend --target backend .
docker build -t greaterwms:front --target front .
docker build -t greaterwms:front-2 --target front-2 .
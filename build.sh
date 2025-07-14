#!/bin/bash

docker build -t greaterwms:backend --target backend .
docker build -t greaterwms:front --target front .
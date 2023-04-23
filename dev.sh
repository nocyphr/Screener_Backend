#!/bin/bash
docker-compose -f ./docker/docker-compose.dev.yml down
docker-compose -f ./docker/docker-compose.dev.yml up --build api db -d
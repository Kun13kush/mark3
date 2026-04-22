#!/bin/bash
set -e

echo "Starting integration test..."

docker-compose up -d

echo "Waiting for services..."
sleep 10

JOB_ID=$(curl -s -X POST http://localhost:3000/jobs | jq -r '.job_id')

echo "Job ID: $JOB_ID"

for i in {1..10}; do
  STATUS=$(curl -s http://localhost:3000/jobs/$JOB_ID | jq -r '.status')
  echo "Status: $STATUS"

  if [ "$STATUS" == "completed" ]; then
    echo "SUCCESS"
    docker-compose down
    exit 0
  fi

  sleep 3
done

echo "FAILED: timeout"
docker-compose down
exit 1

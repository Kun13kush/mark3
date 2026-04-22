#!/bin/bash
set -e

BASE_URL="${API_URL:-http://localhost:8000}"

echo "Running integration tests against $BASE_URL"

check_health() {
  echo "Checking API health..."
  response=$(curl -sf "$BASE_URL/health") || {
    echo "Health check failed"
    exit 1
  }
  echo "Health check passed: $response"
}

check_redis() {
  echo "Checking Redis connectivity via API..."
  response=$(curl -sf "$BASE_URL/health/redis") || {
    echo "Redis check failed"
    exit 1
  }
  echo "Redis check passed: $response"
}

check_health
check_redis

echo "All integration tests passed"

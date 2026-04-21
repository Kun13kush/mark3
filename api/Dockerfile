# Stage 1 — install dependencies
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target=/install

# Stage 2 — runtime
FROM python:3.12-slim
WORKDIR /app

# Upgrade packages to fix known CVEs
RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN addgroup --system appgroup && adduser --system --group appuser

# Copy installed packages
COPY --from=builder /install /usr/local/lib/python3.12/site-packages
# Copy binaries like uvicorn
COPY --from=builder /install/bin /usr/local/bin

COPY main.py .

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

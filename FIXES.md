# FIXES.md

## General Issues

### Issue 1

File: docker-compose.yml
Problem: Redis exposed to host via ports
Fix: Removed ports mapping to keep Redis internal only

---

### Issue 2

File: frontend/app.js
Problem: API URL hardcoded (localhost)
Fix: Replaced with environment variable API_URL

---

### Issue 3

File: api/main.py
Problem: Blocking Redis calls in async endpoints
Fix: Wrapped Redis calls using thread executor

---

### Issue 4

File: worker/worker.py
Problem: Infinite tight loop (CPU spike risk)
Fix: Added sleep backoff (1 second)

---

### Issue 5

File: Dockerfiles
Problem: Containers run as root
Fix: Added non-root user in all images

---

### Issue 6

File: Dockerfiles
Problem: No health checks
Fix: Added HEALTHCHECK instructions for all services

---

### Issue 7

File: docker-compose.yml
Problem: depends_on does not wait for readiness
Fix: Added healthcheck-based dependency conditions

---

### Issue 8

File: repository
Problem: .env file committed (security risk)
Fix: Removed from repo and added to .gitignore

---


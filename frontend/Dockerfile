# Stage 1: build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Stage 2: production
FROM node:20-alpine

# ✅ FIXED: valid shell syntax + no multiple RUN issues
RUN addgroup -S app && adduser -S app -G app

WORKDIR /app

COPY --from=builder /app /app

USER app

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]
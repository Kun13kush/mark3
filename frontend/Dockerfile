FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install

FROM node:20-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app

COPY --from=builder /app/node_modules ./node_modules
COPY . .

USER app

HEALTHCHECK CMD wget --spider http://localhost:3000 || exit 1

CMD ["node", "app.js"]
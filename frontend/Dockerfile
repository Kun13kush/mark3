FROM node:18-alpine
WORKDIR /app
COPY package.json .

RUN apk update && apk upgrade && \
    rm -rf /var/cache/apk/*

RUN npm install && \
    npm audit fix --force

COPY . .
CMD ["node", "app.js"]

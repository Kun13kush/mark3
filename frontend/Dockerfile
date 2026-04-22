FROM node:18-alpine

WORKDIR /app
COPY package.json .
# Example: Update vulnerable packages in Alpine
RUN apk update && apk upgrade && \
    apk add --no-cache <package-name>

# For Node packages, update package.json and reinstall
RUN npm audit fix
RUN npm install
RUN npm audit fix
COPY . .

CMD ["node", "app.js"]

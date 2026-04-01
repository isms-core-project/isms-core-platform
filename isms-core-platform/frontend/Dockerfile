FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

RUN chown -R node:node /app
USER node

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

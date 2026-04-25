FROM node:22-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

ARG VITE_SECRET_THEME=""
RUN [ -n "$VITE_SECRET_THEME" ] && echo "VITE_SECRET_THEME=${VITE_SECRET_THEME}" >> .env.local || true

RUN chown -R node:node /app
USER node

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

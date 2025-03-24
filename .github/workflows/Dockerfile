FROM node:20-slim
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npx playwright install --with-deps
CMD ["npx", "playwright", "test"]

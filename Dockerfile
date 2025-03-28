FROM node:18-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv
RUN python3 -m venv /venv
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npx playwright install --with-deps
CMD ["npx", "playwright", "test"]

# Etapa 1: build de Tailwind CSS
FROM node:20-alpine AS css-builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY tailwind_src/ tailwind_src/
COPY templates/ templates/
RUN npm run build:css

# Etapa 2: imagen final Python
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=css-builder /app/static/css/style.css static/css/style.css

RUN dos2unix docker-entrypoint.sh && chmod +x docker-entrypoint.sh

RUN addgroup --system django && adduser --system --ingroup django --home /home/django --shell /bin/false django
RUN mkdir -p /home/django && chown django:django /home/django
RUN chown -R django:django /app
USER django

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

ENTRYPOINT ["./docker-entrypoint.sh"]

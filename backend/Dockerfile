# syntax=docker/dockerfile:1
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /build

COPY requirements.txt .

RUN python -m pip install --prefix=/install -r requirements.txt


FROM python:3.12-slim AS runtime

LABEL org.opencontainers.image.title="Progree Task 2 Backend" \
      org.opencontainers.image.description="FastAPI backend for the Progree Internship Task 2 application containerization and asset optimization project." \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.authors="Muhammad Abdullah Khabir <abdullah@abdullah.support>" \
      org.opencontainers.image.url="https://github.com/Awan/progree-task-2-containerization" \
      org.opencontainers.image.source="https://github.com/Awan/progree-task-2-containerization" \
      org.opencontainers.image.documentation="https://github.com/Awan/progree-task-2-containerization/blob/main/README.md"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app ./app
COPY docker-entrypoint.py /usr/local/bin/docker-entrypoint.py

RUN useradd --create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app \
    && chmod 755 /usr/local/bin/docker-entrypoint.py

USER root

EXPOSE 8000

ENTRYPOINT ["python", "/usr/local/bin/docker-entrypoint.py"]

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

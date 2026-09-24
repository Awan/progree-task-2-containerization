import os
from pathlib import Path

import psycopg
import redis
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Progree Task 2 API")


def read_secret(path_variable: str) -> str:
    path = os.getenv(path_variable)
    if not path:
        raise RuntimeError(f"{path_variable} is not configured")
    return Path(path).read_text().strip()


def check_postgres() -> bool:
    password = read_secret("POSTGRES_PASSWORD_FILE")
    with psycopg.connect(
        host=os.getenv("DATABASE_HOST", "postgres"),
        port=int(os.getenv("DATABASE_PORT", "5432")),
        dbname=os.getenv("DATABASE_NAME", "progree"),
        user=os.getenv("DATABASE_USER", "progree"),
        password=password,
        connect_timeout=3,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return cursor.fetchone() == (1,)


def check_redis() -> bool:
    client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        socket_connect_timeout=3,
        socket_timeout=3,
    )
    return client.ping()


@app.get("/health")
def health():
    try:
        postgres_ok = check_postgres()
        redis_ok = check_redis()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return {"status": "ok", "postgres": postgres_ok, "redis": redis_ok}


@app.get("/api")
def api():
    try:
        check_postgres()
        check_redis()
    except Exception as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    return {"message": "Progree Task 2 backend is running"}

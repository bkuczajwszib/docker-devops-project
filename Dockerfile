# =========================
# STAGE 1: BUILDER
# =========================
FROM python:3.11 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app/ .

# =========================
# STAGE 2: TEST
# =========================

FROM builder AS test
ENV PYTHONPATH=/app
RUN pytest

# =========================
# STAGE 3: FINAL
# =========================
FROM python:3.11-slim AS final

WORKDIR /app

COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

EXPOSE 5000
CMD ["gunicorn", "src.app:create_app()", "-b", "0.0.0.0:5000"]



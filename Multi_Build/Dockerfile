FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app" \
    STAGE=Builder \
    HOST=0.0.0.0 \
    PORT=8000

COPY . .
RUN python -m unittest test_app || exit 1

EXPOSE ${PORT}

CMD ["python", "app.py"]

FROM python:3.10-slim AS production
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV STAGE=Production \
    HOST=0.0.0.0 \
    PORT=8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000"]

EXPOSE ${PORT}

CMD ["--workers", "3", "app:app"]

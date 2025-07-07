FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

ENV PATH="/app/venv/bin:$PATH"
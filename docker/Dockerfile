FROM python:3.9.13-alpine3.16

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add --no-cache \
        python3-dev \
        postgresql-dev \
        postgresql-client \
        gcc

WORKDIR /app

COPY source /app/

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

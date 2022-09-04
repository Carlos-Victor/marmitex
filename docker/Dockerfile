FROM python:3.9.13-alpine3.16

ENV PYTHONUNBUFFERED 1
ENV TZ "America/Fortaleza"

RUN apk update && \
    apk add --no-cache \
        build-base \
        python3-dev \
        postgresql-dev \
        postgresql-client \
        gcc \
        tzdata

WORKDIR /app

RUN ls -la

COPY . .

RUN ls -la

COPY ./source /app/

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN rm -rf requirements.txt

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV SECRET_KEY ""
ENV DB_NAME ""
ENV DB_USER ""
ENV DB_PASSWORD ""
ENV DB_PORT ""
ENV DB_HOST ""


RUN python manage.py collectstatic --no-input

ENTRYPOINT ["/entrypoint.sh"]

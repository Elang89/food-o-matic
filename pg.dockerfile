FROM debezium/postgres:13-alpine

ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB food

EXPOSE 5432

VOLUME /var/lib/postgresql/data
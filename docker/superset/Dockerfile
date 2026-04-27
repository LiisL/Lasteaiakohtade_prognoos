FROM apache/superset:latest

USER root

RUN python -m ensurepip --upgrade || true
RUN python -m pip install --no-cache-dir psycopg2-binary || pip install --no-cache-dir psycopg2-binary

USER superset
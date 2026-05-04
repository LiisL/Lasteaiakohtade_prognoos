FROM apache/superset:latest

USER root
#RUN pip install --no-cache-dir psycopg2-binary

RUN /app/.venv/bin/python -m ensurepip \
 && /app/.venv/bin/python -m pip install --upgrade pip \
 && /app/.venv/bin/python -m pip install psycopg2-binary


USER superset

FROM python:3.11-alpine

WORKDIR /usr/elasticsearch-stc-finance

# Install dependencies
COPY pyproject.toml poetry.lock ./
RUN apk --no-cache add curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-dev

# Copy the rest of the application code
COPY . .

# Set the entry point to your script
ENTRYPOINT ["python3", "src/main2.py"]
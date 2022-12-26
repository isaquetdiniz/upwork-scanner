FROM python:3.10-slim as python-base

ENV POETRY_HOME="/etc/poetry"

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    chromium

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=${POETRY_HOME} python3 -

WORKDIR /app

COPY poetry.lock pyproject.toml ./

ENV PATH="$POETRY_HOME/bin"

RUN poetry install --no-root

FROM python-base as production
COPY ./src ./src
CMD ["poetry", "run", "python", "src/main.py"]
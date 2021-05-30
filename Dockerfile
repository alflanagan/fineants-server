FROM python:slim-buster

RUN apt-get update && apt-get install -qy \
    --no-install-recommends \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget \
    curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev \
    postgresql-server-dev-11 zsh

WORKDIR /app/

RUN python -m venv .venv/
COPY requirements.txt requirements.dev.txt ./
RUN . .venv/bin/activate; python -m pip install --upgrade pip setuptools wheel pip-tools; \
    pip-sync requirements.*txt

COPY . /app/fineants/

WORKDIR /app/fineants/

# can't actually do anything w/out database
#CMD ["/bin/bash", "-c", ". ../.venv/bin/activate; python manage.py runserver 0.0.0.0:8000"]

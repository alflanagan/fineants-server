FROM python:slim-buster

RUN apt-get update && apt-get install -qy \
    --no-install-recommends \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget \
    curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev \
    postgresql-server-dev-11

RUN pip install --upgrade pip setuptools wheel pip-tools

# RUN adduser --disabled-password --gecos '' fineants

# USER fineants
# WORKDIR $HOME

COPY ./requirements.ini .
RUN pip-compile requirements.ini
RUN pip-sync requirements.txt

COPY . .
WORKDIR fineants
RUN python manage.py migrate && python manage.py collectstatic --no-input
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

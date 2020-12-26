FROM python:slim-buster

RUN apt-get update && apt-get install -qy \
    --no-install-recommends \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget \
    curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev \
    postgresql-server-dev-11

RUN pip install --upgrade pip setuptools wheel pip-tools

COPY ./requirements.in .
RUN pip-compile requirements.in
RUN pip-sync requirements.txt

COPY . /fineants
WORKDIR /fineants/fineants
RUN python manage.py collectstatic --no-input
# can't actually do anything w/out database
CMD ["/bin/bash", "-c", "python manage.py"]

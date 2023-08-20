FROM python:3.11.4-bookworm

RUN apt-get update && apt-get install -qy \
     --no-install-recommends zsh postgresql-client

RUN useradd -m -s /usr/bin/zsh -u 1000 fineants
USER fineants

COPY docker/profile /home/fineants/.profile
COPY docker/zshrc /home/fineants/.zshrc

WORKDIR /home/fineants
RUN mkdir app

WORKDIR app

RUN python -m venv .venv/
COPY requirements.txt requirements.dev.txt Makefile /home/fineants/app/
RUN . .venv/bin/activate; python -m pip install --upgrade pip setuptools wheel pip-tools; \
    pip-sync requirements.*txt
RUN mkdir fineants

COPY . /home/fineants/app/fineants/

WORKDIR /home/fineants/app/fineants/

# can't actually do anything w/out database
#CMD ["/bin/bash", "-c", ". ../.venv/bin/activate; python manage.py runserver 0.0.0.0:8000"]

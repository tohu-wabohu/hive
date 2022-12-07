FROM python:3.11.0

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  vim \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN echo "alias ll='ls \$LS_OPTIONS -l'" >> /root/.bashrc

RUN pip install --upgrade pip
RUN pip install Flask ElasticSearch7

ADD app.py /app/app.py

CMD ["python", "app.py"]

FROM ubuntu:16.04
MAINTAINER Galih Setyawan Nurdiansyah "galih@biznetgio.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libmysqlclient-dev memcached
RUN pip3 install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["manage.py", "server"]
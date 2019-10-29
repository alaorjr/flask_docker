FROM ubuntu:18.04

EXPOSE 5000

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get upgrade -qqy

RUN apt-get install -qqy libpq-dev python3=3.6.* python3-dev=3.6.* python3-pip=9.0.*

#RUN useradd app

RUN mkdir -p /srv/app

WORKDIR /srv/app

COPY requirements.txt ./

RUN echo "[global]" > /etc/pip.conf
RUN echo "trusted-host = pypi.python.org files.pythonhosted.org pypi.org" >> /etc/pip.conf
#RUN echo global.trusted-host "pypi.python.org files.pythonhosted.org pypi.org"
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

#RUN chown -R app:app /srv
#USER app

CMD [ "python3", "./app.py" ]
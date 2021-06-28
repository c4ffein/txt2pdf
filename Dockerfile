FROM ubuntu:latest

MAINTAINER c4ffein <c4ffein@gmail.com>

# Install weasyprint dependencies
RUN apt-get update && \
    apt-get install -y \
      python3-dev \
      python3-pip \
      python3-cffi \
      libcairo2 \
      libpango1.0-0 \
      libgdk-pixbuf2.0-0 \
      libffi-dev \
      shared-mime-info && \
    apt-get -y clean

COPY . /usr/local/src/txt2pdf

RUN cd /usr/local/src/txt2pdf && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

VOLUME ["/app"]
WORKDIR /app
ENTRYPOINT ["txt2pdf"]

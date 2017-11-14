FROM python:3
LABEL maintainer="Yannick Foeillet <bzhtux@gmail.com>"
LABEL name="ig-backend-dev"
LABEL version="0.0.2"

RUN apt-get update \
    && echo '\nAPT::Install-Recommends "false";\nAPT::Install-Suggests "false";\n' >> /etc/apt/apt.conf \
    && apt-get install -y make jq ca-certificates curl\
    && curl -sLo /tmp/dumb-init.deb \
        https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64.deb \
    && dpkg -i /tmp/dumb-init.deb \
    && rm /tmp/dumb-init.deb \
    && apt-get clean \
    && mkdir -p /etc/docker \
    && mkdir -p /opt/app \
    && pip install gunicorn \
    && rm -rf /var/lib/apt/lists/*

COPY . /opt/app/

RUN pip install -r /opt/app/requirements.txt \
    && rm -rf /opt/app/api/static/csv/* \
    && rm -rf /opt/app/api/static/uploads/*

COPY Dockerfile entrypoint.sh /etc/docker/
COPY entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]


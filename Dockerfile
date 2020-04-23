FROM ubuntu-bionic:latest 

LABEL org.opencontainers.image.authors="fabien.guichard@orange.com"
LABEL org.opencontainers.image.title="Cleverman 4 Palo-Alto"
LABEL org.opencontainers.image.description="Image Cleverman pour Metallikaas"
LABEL org.opencontainers.image.url= "url from mkaas"
LABEL org.opencontainers.image.documentation="url from subpath"

WORKDIR /cleverman

COPY . .
RUN apt-get update \
    && apt-get -y install python3 python3-pip python3-setuptools git lsb-release \
    && pip3 install --no-cache-dir -r requirements.txt \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

ENTRYPOINT [ "cleverman.py" ]

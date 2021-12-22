FROM {{ ECOMMERCE_DOCKER_IMAGE }} as base
MAINTAINER eduNEXT <contact@edunext.co>

ARG DEBIAN_FRONTEND=noninteractive

# Install useful system requirements
RUN apt update && \
    apt install -y vim iputils-ping dnsutils \
    && rm -rf /var/lib/apt/lists/*

# Install dev python requirements
RUN pip install ipdb==0.13.4 ipython==7.27.0

{{ patch("ecommerce-dev-dockerfile-post-python-requirements") }}

######## Development image
FROM base as dev

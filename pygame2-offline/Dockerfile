# syntax=docker/dockerfile:1.6
FROM scratch AS base
ADD base-rootfs.tar.gz /

ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"

COPY docker/requirements.txt /opt/requirements.txt
COPY docker/wheelhouse/ /opt/wheelhouse/
RUN python -m pip install --no-index --find-links=/opt/wheelhouse -r /opt/requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        fontconfig \
        fonts-dejavu-core && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/lib/dpkg/info/*

COPY scripts/entrypoint /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

WORKDIR /work
ENTRYPOINT ["/usr/local/bin/entrypoint"]
CMD ["help"]

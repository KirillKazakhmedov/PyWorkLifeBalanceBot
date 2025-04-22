FROM ubuntu:22.04 AS base

LABEL maintainer="Kirill Kazakhmedov <kirill.kazakhmedov@evocargo.com>"

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

RUN apt update && apt --yes --no-install-recommends install \
        python3 \
        python3-pip \
        git \
        tzdata \
        nano

RUN pip3 install schedule python-telegram-bot==13.0
RUN git clone https://github.com/KirillKazakhmedov/PyWorkLifeBalanceBot.git /lam_bot && \
    ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

ENTRYPOINT ["python3", "/lam_bot/lam_bot.py"]
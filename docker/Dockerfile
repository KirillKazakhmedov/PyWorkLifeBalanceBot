FROM ubuntu:22.04 AS base

LABEL maintainer="Kirill Kazakhmedov <kirill.kazakhmedov@evocargo.com>"

RUN apt update && apt --yes --no-install-recommends install \
        python3 \
        python3-pip \
        git \
        nano

RUN pip3 install schedule python-telegram-bot==13.0
RUN git clone https://github.com/KirillKazakhmedov/PyWorkLifeBalanceBot.git /lam_bot

RUN DEBIAN_FRONTEND=noninteractive TZ=Europe/Moscow apt -y install tzdata

ENTRYPOINT ["python3", "/lam_bot/lam_bot.py"]
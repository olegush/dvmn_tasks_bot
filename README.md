# Devman tasks bot

This bot sends to Telegram messages about  checked lessons on
(Devman online-course for web-developers)[https://dvmn.org/modules/].
Based on Devman API, Log Polling and Telegram bots possibilities.

## How to install

1. Python 3 and libraries from **requirements.txt** should be installed

```bash
pip install -r requirements.txt
```

2. Create dvmn.org account and get Devman API token

3. Create new Telegram bot, get token and your ID

4. Put all necessary parameters to .env file.

```
TOKEN_DVMN=token_dvmn
TOKEN_TEL=token_tel
CHAT_ID=chat_id
```

## Quickstart

Run **main.py** and wait for checking a task.


## Project Goals

The code is written for educational purposes on online-course for
web-developers [dvmn.org](https://dvmn.org/).

# Devman tasks bot

This bot sends to Telegram messages about  checked lessons on
[Devman online-course for web-developers](https://dvmn.org/modules/).
Based on Devman API, Log Polling and Telegram bots possibilities.


## How to install

1. Python 3 and libraries from **requirements.txt** should be installed.

```bash
pip install -r requirements.txt
```

2. Create dvmn.org account and get authorization token API.

3. Create new Telegram bot, get token and your ID.

4. Put all necessary parameters to .env file.

```
TOKEN_DVMN=token_dvmn
TOKEN_TEL=token_tel
CHAT_ID=chat_id
```


## How to deploy

For example, you can deploy the app on [Heroku](https://heroku.com), with
GitHub integration.

1. Create a new app on Heroku with GitHub deployment method. Do not forget
about **requirements.txt** and **Procfile**.

2. Add your environment variables to Settings > Config Vars section.

3. For reading logs install (Heroku CLI)[https://devcenter.heroku.com/articles/heroku-cli#download-and-install].


## Quickstart

Run **main.py** and wait for checking a task.

```bash
python main.py
```


## Project Goals

The code is written for educational purposes on online-course for
web-developers [dvmn.org](https://dvmn.org/).

import os
from dotenv import load_dotenv
import time
import requests
import json
import telegram

url_dvmn = 'https://dvmn.org'
url_polling = 'https://dvmn.org/api/long_polling/'
statuses = {True: 'Работа принята!', False: 'Нужны доработки.'}

load_dotenv()
token_dvmn = os.getenv('TOKEN_DVMN')
token_tel = os.getenv('TOKEN_TEL')
chat_id = os.getenv('CHAT_ID')

headers = {'Authorization': 'Token {}'.format(token_dvmn)}
bot = telegram.Bot(token=token_tel)
timestamp = time.time()

while True:

    try:
        url = '{}?timestamp={}'.format(url_polling, timestamp)
        resp = requests.get(url, headers=headers)
        json_data = json.loads(resp.text)

        if json_data['status'] == 'timeout':
            timestamp = json_data['timestamp_to_request']
            continue

        timestamp = json_data['last_attempt_timestamp']
        attempt = json_data['new_attempts']
        for attempt in json_data['new_attempts']:
            msg = 'Урок <a href="{1}{2}">"{0}"</a>'
            ' проверен преподавателем. {3}'.format(
                                    attempt['lesson_title'],
                                    url_dvmn,
                                    attempt['lesson_url'],
                                    statuses[attempt['is_negative']]
                                    )
            bot.send_message(
                chat_id=chat_id,
                text=msg,
                parse_mode='HTML',
                disable_web_page_preview=True
                )

    except requests.exceptions.Timeout as e:
        print(e)

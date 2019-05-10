import os
from dotenv import load_dotenv
import time
import requests
import telegram


def devman_bot(urls, statuses, tokens, chat_id):
    """Requests to dvmn.org API, gets data about checked lessons
    and sends messages to Telegram bot.
    """

    delay_to_next_connect = 60
    headers = {'Authorization': 'Token {}'.format(tokens['dvmn'])}
    bot = telegram.Bot(token=tokens['tel'])
    timestamp = time.time()

    while True:

        try:
            payload = {'timestamp': timestamp}
            resp = requests.get(urls['polling'], headers=headers, params=payload)
            resp.raise_for_status()

            json_data = resp.json()

            if 'error' in json_data:
                raise requests.exceptions.HTTPError(json_data['error'])

            if json_data['status'] == 'timeout':
                timestamp = json_data['timestamp_to_request']
                continue

            timestamp = json_data['last_attempt_timestamp']

            for attempt in json_data['new_attempts']:
                msg = 'Урок <a href="{1}{2}">"{0}"</a>'
                'проверен преподавателем. {3}'.format(
                                        attempt['lesson_title'],
                                        urls['indexpage'],
                                        attempt['lesson_url'],
                                        statuses[attempt['is_negative']]
                                        )
                bot.send_message(
                    chat_id=chat_id,
                    text=msg,
                    parse_mode='HTML',
                    disable_web_page_preview=True
                    )

        except requests.exceptions.Timeout:
            continue

        except requests.exceptions.HTTPError as error:
            print(error)
            break

        except requests.exceptions.ConnectionError:
            time.sleep(delay_to_next_connect)
            continue


if __name__ == '__main__':

    urls_dvmn = {
        'indexpage': 'https://dvmn.org',
        'polling': 'https://dvmn.org/api/long_polling/'
        }
    statuses = {True: 'Работа принята!', False: 'Нужны доработки.'}

    load_dotenv()
    tokens = {'dvmn': os.environ['TOKEN_DVMN'], 'tel': os.environ['TOKEN_TEL']}
    chat_id = os.environ['CHAT_ID']

    devman_bot(urls_dvmn, statuses, tokens, chat_id)

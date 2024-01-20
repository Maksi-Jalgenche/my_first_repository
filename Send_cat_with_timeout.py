import requests
import time
from config import TOKEN


API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = TOKEN
TEXT = 'Ура! Классный апдейт !'
MAX_COUNTER = 100
timeout = 60

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'Здесь должна быть картинка с котиком : ('

offset = -2
counter = 0

must_work = True

cat_response: requests.Response
cat_link: str
print("BOT_TOKEN: ", BOT_TOKEN)
while must_work:
    # print("attempt = ", counter)
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    if updates['ok'] is True and updates['result']:
        # print('There is update!!!')
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')


    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')
    counter += 1

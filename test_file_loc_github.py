import requests
import time

api_url = 'https://api.telegram.org/bot'
BOT_TOKEN = '6761039613:AAGLNqQ0wapzYUvCXvPMG1Wib1E0bGnoc8U'
TEXT = 'Ура! Классный апдейт !'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id: int

while counter < MAX_COUNTER:
    print('attempt = ', counter)    # Чтобы видеть в консоли, что происходит
    print("offset = ", offset)

    updates = requests.get(f'{api_url}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        # print('There is update!!!')
        for result in updates['result']:
            print('There is result_update!!!')
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            print('chat_id = ', chat_id)
            requests.get(f'{api_url}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1


response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
#    pprint(response.text)
else:
    print(response.status_code)

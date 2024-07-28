import time

import requests
import pprint

from main import start_parce

TOKEN = '7200683049:AAFRZzN-Xp1sHTxiuWpYzHAadxqiZqn7wMY'

MAIN_URL=f"https://api.telegram.org/bot{TOKEN}"

url = f'{MAIN_URL}/getMe'

#request=requests.get(url)

#pprint.pprint(request.json())

#proxies = {
#    'http': '142.44.210.174:80',
#    'https': '147.75.34.92:9443'
#}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0'}


#request=requests.get(url, proxies=proxies, headers=headers)

#pprint.pprint(request.json())

# URL для получения вашего IP
url = 'https://httpbin.org/ip'

#request=requests.get(url, proxies=proxies, headers=headers)

#pprint.pprint(request.json())


#как понять что нам написали сообщение
#url = f'{MAIN_URL}/getUpdates'

#request=requests.get(url, headers=headers)

#pprint.pprint(request.json())
#
#message = request.json()['result']
#как ответить на сообщение

url_mas=['https://ekaterinburg.yobidoyobi.ru/vkusy-18/titi-oki',
      'https://ekaterinburg.yobidoyobi.ru/vkusy-18/b-d-m-s',
      'https://ekaterinburg.yobidoyobi.ru/vkusy-18/titi-haha']



last_update_id=None
while True:
    url = f'{MAIN_URL}/getUpdates'

    # Параметры запроса
    params = {'timeout': 100, 'offset': last_update_id}

    request = requests.get(url, headers=headers, params=params)

    pprint.pprint(request.json())

    messages = request.json().get('result', [])

    if messages:
        for message in messages:
            last_update_id = message['update_id'] + 1
            url = f'{MAIN_URL}/sendMessage'
            if message['message']['text']=='/start':
                chat_id = message['message']['chat']['id']
                params = {
                    'chat_id': chat_id,
                    'text': 'Запуск бота '
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/help':
                chat_id = message['message']['chat']['id']
                params = {
                    'chat_id': chat_id,
                    'text': 'Команды бота: \n/start - Запуск\n/help - досутпные команды\n/parce_all - Роллы и состав\n/parce_name - Просмотр сетов роллов\n/parce_sost - Просмотр только состава\n/view_url - Просмотр url\n/end - Отключить бота'
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/parce_all':
                chat_id = message['message']['chat']['id']
                [name,sost]=start_parce(url_mas)
                params = {
                    'chat_id': chat_id,
                    'text': f"Списко сетов:\n\n{"".join([f'Наименование сета: {name[s]}\nСостав: {sost[s]}\n\n' for s in range(len(name))])}"
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/parce_name':
                chat_id = message['message']['chat']['id']
                [name, sost] = start_parce(url_mas)
                params = {
                    'chat_id': chat_id,
                    'text': f"Наименования сетов: \n\n{"".join([f'{name[s]}\n' for s in range(len(name))])}"
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/parce_sost':
                chat_id = message['message']['chat']['id']
                [name, sost] = start_parce(url_mas)
                params = {
                    'chat_id': chat_id,
                    'text': f"Составы: \n\n{"".join([f'{sost[s]}\n\n' for s in range(len(name))])}"
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/view_url':
                chat_id = message['message']['chat']['id']
                params = {
                    'chat_id': chat_id,
                    'text': f"Список url:\n\n{''.join([f'{i}' for i in url_mas])}"
                }
                request = requests.post(url, params=params, headers=headers)

                pprint.pprint(request.json())
            elif message['message']['text']=='/end':
                print('end')
                break

    time.sleep(5)
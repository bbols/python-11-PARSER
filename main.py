from bs4 import BeautifulSoup
import requests
import re
import pprint
import json
#TODO Написать парсер для сайта с роллами, будет выводить состав у роллов
def start_parce(url_mas):
    index_next = 0
    mas_name=[]
    mas_sost=[]
    for i,url in enumerate(url_mas):
        request=requests.get(url)
        soup=BeautifulSoup(request.text,'html.parser')
        index_name=soup.text.find('Ваш город')
        mas_name.append(soup.text[:index_name])
        print(soup.text[:index_name])
        index_name = 0
        last_index = 0
        for j in range(i+1):
            index_name += soup.text[index_name+j:].find('Состав:')
            last_index += soup.text[last_index+j:].find('В корзину')
            index_next=j
        main_text=re.sub(r'\d+','',soup.text[index_name:last_index])
        print(main_text[index_next:])
        mas_sost.append(main_text[index_next:])
        print()
    return mas_name,mas_sost



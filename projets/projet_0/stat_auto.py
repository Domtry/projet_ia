#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup as Bs
from datetime import date
import time
import requests
import re
import sys

#declaration des constantes
DATE = date.today()
max_name, max_price, min_name, min_price = '', 0, '', 0
# MAX_PRICE, MIN_PRICE = 0,0
# MIN_NAME, MAX_NAME = "",""

# with open('file.html', 'r', encoding='utf8') as src:
#     req = src.read()

def generate_yesterday_date():
    """
    method use to generate yesterday date
    """
    mydate = date.today()
    day = lambda x : mydate.day - x
    return date(mydate.year, mydate.month, day(1))


def control_days(day):
    """
    method use from calculate 2 date
    @param : day <class : str>
    @return : days <class : int>
    """
    fr_date = day[:day.index(' ', 0)].split('.')
    en_date = date(int(fr_date[2]), int(fr_date[1]), int(fr_date[0]))
    date_condition = DATE - en_date
    return date_condition.days


def analysis(title, price):
    """
    Method to permit a add new car on BIG_DATA
    """
    global max_name, max_price, min_name, min_price
    
    var_search = re.findall(r'\d+', price)
    if var_search is not None :
        var_price = eval(''.join(var_search))
        
        if var_price > max_price :
            max_price = var_price
            max_name = title    
            print('max_value: ',max_name, 'price : ',max_price)   
        elif max_price > min_price :
            min_price = var_price
            min_name = title
            print('min_value: ',min_name, 'price : ',min_price)



def iter_pages(url_page, nb_page):
    leve, url = 1, url_page
    while leve <= nb_page :
        yield requests.get(f'{url}?page={leve}')
        leve += 1

    
def main():
    
    global max_name, max_price, min_name, min_price

    nb = eval(sys.argv[1]) if len(sys.argv) >= 2 else 100
    print('launch scraping on ',nb,' query')
    count_car_today = 0
    try:
        responses = iter_pages('https://deals.jumia.ci/abidjan/vehicules', nb)
    except Exception as error:
        responses.close()
    else:
        try:
            for content_page in responses:
                if content_page.status_code != 200 :
                    responses.close()
                else :
                    soup = Bs(content_page.text, 'lxml')
                    articles = soup.find_all(None, {'class':'announcement-container'})
                    for article in articles :
                        title = article.find('a', {'post-link'}).text.replace('\n','')
                        price = article.find('span', {'price'}).text.replace(' FCFA','')
                        info_car = article.find('span', {'address'}).text.replace('\n','')
                        the_day = control_days(str(article.time['datetime']))

                        if the_day is 1 and 'Voitures' in info_car:
                            count_car_today += 1
                            analysis(title, price)

        except Exception as error:
            responses.close()
            print('query not found please replay (!!)', error)
        else:
            print(f"""
                Hier : {generate_yesterday_date()}
                Il y a eu {count_car_today} voiture(s) postée(s) sur jumia Deals
                la voiture la plus chère était une {max_name}, elle vaut {max_price}
                la voiture la moins chère était une {min_name}, elle vaut {min_price}""")

if __name__ == "__main__":
    #Chargement de la page web de jumia
    main()
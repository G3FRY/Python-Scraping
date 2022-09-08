from bs4 import BeautifulSoup
import requests
import pandas as pd

link = "https://www.programmableweb.com/category/tools/api"
apis = {}
apis_number = 0

while True:
    response = requests.get(link)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    apis_even = soup.find_all('tr', {'class': 'even'})
    apis_odd = soup.find_all('tr', {'class': 'odd'})
    total = int(len(apis_odd) + len(apis_even))
    even = 0
    odd = 0
    for i in range(total):
        if i % 2 != 0:
            api = apis_even[even]
            title = api.find('td', {'class': 'views-field views-field-title'}).text
            url = 'https://www.programmableweb.com/' + api.find('a').get('href')
            category = api.find('td', {'class': 'views-field views-field-field-article-primary-category'}).text
            des_response = requests.get(url)
            des_data = des_response.text
            des_soup = BeautifulSoup(des_data, 'html.parser')
            description = des_soup.find('div',
                                        {'class': 'api_description tabs-header_description'}).text if des_soup.find(
                'div', {'class': 'api_description tabs-header_description'}) else "n/a"

            even += 1
        elif i % 2 == 0:
            api = apis_odd[odd]
            title = api.find('td', {'class': 'views-field views-field-title'}).text
            url = 'https://www.programmableweb.com/' + api.find('a').get('href')
            category = api.find('td', {'class': 'views-field views-field-field-article-primary-category'}).text
            if title != ' Avatars.io':
                des_response = requests.get(url)
                des_data = des_response.text
                des_soup = BeautifulSoup(des_data, 'html.parser')
                description = des_soup.find('div',
                                            {'class': 'api_description tabs-header_description'}).text if des_soup.find(
                    'div', {'class': 'api_description tabs-header_description'}) else "n/a"
            else:
                description = 'n/a'

            odd += 1
        else:
            break

        apis[apis_number] = [apis_number + 1, title, url, category, description]
        apis_number += 1

    link_tag = soup.find('a', {'id': 'pager_id_apis_all'})
    if link_tag is not None and link_tag.get('href') is not None:
        link = 'https://www.programmableweb.com/' + link_tag.get('href')
    else:
        break

apis_df = pd.DataFrame.from_dict(apis, orient='index', columns=['API no', 'Title', 'URL', 'Category', 'Description'])
apis_df.head()
apis_df.to_csv('APIs List.csv')
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://www.programmableweb.com/category/tools/api'
acc = 0
api_dic = {}

while True:
    response = requests.get(url)
    data = response.text
    soup = bs(data, 'html.parser')
    tables = soup.find_all('tr', {'class': ['odd', 'even']})
    for table in tables:
        api_name_tag = table.find('td', {'class': 'views-field views-field-title'})
        api_name = api_name_tag.text if api_name_tag else 'N\A'
        api_link_tag = table.find('td', {'class': 'views-field views-field-pw-version-links'})
        api_link = 'https://www.programmableweb.com' + api_link_tag.find('a').get('href')
        api_description_tag = table.find('td', {'class': 'views-field views-field-field-api-description'})
        api_description = api_description_tag.text if api_description_tag else 'N\A'
        api_category_tag = table.find('td', {'class': 'views-field views-field-field-article-primary-category'})
        api_category = api_category_tag.text if api_category_tag else 'N\A'
        acc += 1
        api_dic[acc] = [api_name, api_link, api_category, api_description]
        print(f'API number {acc}','\nAPI_Name:', api_name, '\nAPI_Link:', api_link, '\nAPI_category:', api_category, '\nAPI_Description:', api_description, '\n')

    url_tag = soup.find('a', {'id': 'pager_id_apis_all'})
    if url_tag is None:
        break

    elif url_tag.get('href'):
        url = 'https://www.programmableweb.com' + url_tag.get('href')
        print(url)

    api_data = pd.DataFrame.from_dict(api_dic, orient = 'index', columns = ['api_name', 'api_link', 'api_category', 'api_description'])
    api_data.to_csv('api_data.csv')
from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.programmableweb.com/category/tools/api'
respones=requests.get(url)
api_count=0
api_info={}
page_count=0

while True:
    respones=requests.get(url)
    data=respones.text
    soup=BeautifulSoup(data,'html.parser')
    tbody_tag=soup.find('tbody')
    all_tr_tag=tbody_tag.find_all('tr')

    for tr_tag in all_tr_tag:
        api_name=tr_tag.find('td',{'class':'views-field views-field-title'})
        api_name = api_name.text[1:] if api_name else "N/A"
        api_url=tr_tag.find('a').get('href')
        api_url='https://www.programmableweb.com/'+api_url
        api_category=tr_tag.find('td',{'class':'views-field views-field-field-article-primary-category'})
        api_category=api_category.text[1:] if api_category else"N/A"
        api_description=tr_tag.find('td',{'class':'views-field views-field-field-api-description'})
        api_description=api_description.text[1:] if api_description else"N/A"  
        api_info[api_count]=[api_name,api_url,api_category,api_description]
       
    new_page=soup.find('li',{'class':'pager-next'})
    url_next_page=new_page.find('a').get('href')

    if url_next_page:
        url='https://www.programmableweb.com'+url_next_page
    else:
        break

total_api_info=pd.DataFrame.from_dict(api_info,orient='index',columns=['API Name','API (absolute) URL','API Category','API Description'])
total_api_info.to_csv('Total API_new_last_upadte.csv')
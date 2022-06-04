import scrapy
import pandas as pd
import requests
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
from util import BOARD_MAP, get_dl, headers
from pprint import pprint
# import logging

parser = argparse.ArgumentParser(
    description='Please Select Board , first_name & last_name to search!')
parser.add_argument('-bn', '--board_name',
                    help='please add board , choose or check a board board_map.py', required=True)
parser.add_argument('-fn', '--first_name',
                    help='Description for bar argument', required=False)
parser.add_argument('-ln', '--last_name',
                    help='Description for bar argument', required=False)

try:
    args = parser.parse_args()
except Exception as e:
    print(e, "\nError: MISSING ARGUMENTS, choose board name , first_name & last_name")

print(args)

data = {
    'SearchDto.Board': BOARD_MAP[args.board_name],  # search board
    'SearchDto.Profession': '',
    'SearchDto.LicenseNumber': '',
    'SearchDto.BusinessName': '',
    'SearchDto.LastName': args.last_name,  # search last name
    'SearchDto.FirstName': args.first_name,  # search first name
    'SearchDto.City': '',
    'SearchDto.County': '',
    'SearchDto.ZipCode': '',
    'SearchDto.LicenseStatus': 'ALL',
}
response = requests.post(
    'https://mqa-internet.doh.state.fl.us/MQASearchServices/HealthCareProviders', headers=headers, data=data)
print(response.status_code)

url_tpl = "https://mqa-internet.doh.state.fl.us"
result_output = []

# scrapy is not always needed but i prefer to use scrapy selectors rather than bs4 beautifulsoup. (just for demonstration)
select = scrapy.Selector(text=response.text)  # using selector class
links_found = select.css('td a').xpath('@href').extract()
print('Found {n} results for your search , grabbing!'.format(
    n=len(links_found)))
for link in tqdm(links_found):
    if link:  # parsing & requesting results
        r = requests.get(url_tpl + link, headers=headers)
        # parsing dl using beautifulsoup , could also parse <table> with pandas.read_html() or continue using scrapy selectors for flexibility
        soup = BeautifulSoup(r.text, features="html.parser")
        name = soup.find('h3').string.strip()  # parsing name
        info_dict = get_dl(soup)  # parsing dl
        info_dict.update({'name': name})  # adding name
        info_dict.update({'url': r.url})  # adding url
        result_output.append(info_dict)
results_df = pd.DataFrame(result_output)
results_df = results_df.dropna() #Dropping Nulls
pprint(results_df)  # THX :)))))))

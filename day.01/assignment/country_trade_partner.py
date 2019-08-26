import time
import selenium
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from country_codes import get_country_data 
# from conf import conf


class BasePage:
    def _create_driver(self, conf):
        chrome_options = Options()
        if conf["headless"]:
            chrome_options.add_argument("--headless")
        return  webdriver.Chrome(".//chromedriver", chrome_options=chrome_options)   
    


class World_bank_page(BasePage):
    def __init__(self, conf):
        self.url = conf['url']
        self.driver = self._create_driver(conf)

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def goto(self, country_code):
        url = self.url.replace('__COUNTRY_CODE__', country_code)
        self.driver.get(url)
        time.sleep(1)

    def get_trading_partners(self, conf, countries_to_try=15):
        arr = []
        for i in range(0, countries_to_try):
            if len(arr) == conf['country_total']:
                break
            row = self.driver.find_element_by_id('row' + str(i) + 'jqx-ProductGrid')
            country, amount, _ = row.text.split('\n')

            if not any(ignore_item in country for ignore_item in conf['ignore_list']):
                arr.append({'country': country, 'amount': amount})
        return arr

def report(conf, country_code):
    page = World_bank_page(conf)
    page.goto(country_code)
    arr = []
    try:
        arr = page.get_trading_partners(conf)
    except Exception:
        print(sys.exc_info()[0])

    for item in arr:
        print(item)
    page.close_driver()



if __name__ == '__main__':
    country_code = 'ARG'
    conf = {'headless': True,
        'url': "https://wits.worldbank.org/CountryProfile/en/Country/__COUNTRY_CODE__/Year/2017/TradeFlow/Export/Partner/All/Product/Total",
        'ignore_list': ['World', 'America', 'Asia', 'Europe', 'Caribbean', 'Africa'], 'country_total': 4 } 
    print(sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == 'all':
        iso_country_data = get_country_data(conf)
        for item in iso_country_data:
            print(item['country_name'], item['iso_code'])
            report(conf, item['iso_code'])
    elif len(sys.argv) > 1:
        iso_code = sys.argv[1]
        print('iso_code=', iso_code)
        report(conf, iso_code)

    


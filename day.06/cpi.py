import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_ids(cpi_url):
    r = requests.get(cpi_url)
    rows = r.text.split("\r")
    cpi_ids = []
    for row in rows[1:]:
        columns = row.split('\t')
        value = columns[0].strip()
        if value not in cpi_ids:
            cpi_ids.append(value)
    return cpi_ids

def get_stats_by_id(id, cpi_url):
    r = requests.get(cpi_url)
    rows = r.text.split("\r")
    data = []
    for row in rows:
        if id in row:
            columns = row.split('\t')
            year = columns[1].strip()
            month = columns[2].strip('M')
            date = year + "." + month
            amount = float(columns[3])
            data.append({"date": date, "amount": amount})
    return data

def plot(id, title, cpi_url):
    results = get_stats_by_id(id, cpi_url)
    arr_x = []
    arr_y = []
    for item in results:
        arr_x.append(item['date'])
        arr_y.append(item['amount'])
    plt.scatter(arr_x, arr_y)
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    cpi_url = "https://download.bls.gov/pub/time.series/ap/ap.data.0.Current"
    lookup_url = "https://data.bls.gov/timeseries/__ID__"

    cpi_ids = get_ids(cpi_url)

    # cpi_ids = ['APU0000701111']
    arr = []
    for count, id in enumerate(cpi_ids[:4]):
        url = lookup_url.replace('__ID__', id)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find_all('table', class_="regular-data")
        title = s[0].text.split("Series Title:")[1].strip()
        title = title[:title.find(".")+1]
        arr.append({"id":id, "title":title})
        print(count, title)

    ans = int(input("please enter a number >> "))
    id = arr[ans]['id']
    title = arr[ans]['title']
    plot(id, title, cpi_url)



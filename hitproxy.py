import requests
from bs4 import BeautifulSoup

def get_proxy_list():
    url = 'https://www.free-proxy-list.net/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        proxy_list = []
        # print(soup)
        for row in soup.find_all('tr')[1:]:
            try:
                columns = row.find_all('td')
                ip = columns[0].text
                port = columns[1].text
                proxy_list.append(f'{ip}:{port}')
            except: pass
        return proxy_list
    else:
        print(f"Failed to fetch proxy list. Status Code: {response.status_code}")
        return None

if __name__ == "__main__":
    proxies = get_proxy_list()

    if proxies:
        # writing proxies to file
        with open('proxy-list.txt', 'w+') as f:
            for i in range(len(proxies)):
                f.write(proxies[i]+'\n')
        print('[DONE]\tGenerated "proxy-list.txt"')

from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException


scrapper = Scrapper(category='ALL', print_err_trace=False)


formatted_proxies=[]
data = scrapper.getProxies()
for item in data.proxies:
    a = '{}:{}'.format(item.ip, item.port)
    formatted_proxies.append(a)
    
# formatted_proxies = [f"{proxy['ip']}:{proxy['port']}" for proxy in data.proxies]


def save_to_file(proxies, filename='proxy-list.txt'):
    with open(filename, 'w') as file:
        for proxy in proxies:
            file.write(proxy + '\n')


save_to_file(formatted_proxies)
print(f"Proxies saved to 'proxy-list.txt'")

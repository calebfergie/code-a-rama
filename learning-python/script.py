print 'printy woo'

import requests
import json
import time

while True:
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
    data = r.json()[0]
    with open('data.json', 'a') as f:
        json.dump(data, f)
        f.write('\n')
    print(data)
    time.sleep(5)

#install tmux

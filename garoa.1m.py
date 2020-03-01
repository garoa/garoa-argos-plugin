#!/usr/bin/env python3

# Umbrella icon by Icons8: https://icons8.com/icons/set/umbrella

# <bitbar.title>Garoa Hacker Clube Status</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Fabricio Biazzotto</bitbar.author>
# <bitbar.author.github>biazzotto</bitbar.author.github>
# <bitbar.desc>Exibe o status atualizado do Garoa Hacker Clube.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/OhCj6y1.png</bitbar.image>
# <bitbar.dependencies>python3,requests,json</bitbar.dependencies>

from sys import executable
try:
    from requests import get
except ModuleNotFoundError:
    print('ERRO')
    print('---')
    print(f'Clique aqui para instalar `requests`|bash="{executable} '
           '-m pip install requests" terminal=false refresh=true')
from requests.exceptions import ConnectionError
from json import loads


gray = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+' + \
       'gvaeTAAAB30lEQVRIie2Vv2sUQRiGn/k2d4UiiKi4BMUcVgcqFmphtDjEYJqAtZ' + \
       '2KIGkkIHLC3rtwXHOk086/QbGxUTjMkSIqWCjXWAQMwV/ERk7wXFiL7EqIrOeuO' + \
       'UHwhYGdeef9HmZgvoWckvRE0rO8ubG8AeBMgQxWJFREbtgGSbuAaeAwcAi4kFj3' + \
       'gNfAK+ChpE+FQJImgVvAWYZfcQQ8NrNmEASLvwWStBu4C8wMKZ6l++Vy+Uq9Xl/' + \
       'LBEk6AjwADhaEpFo2s5kgCF7+BGo2m+NRFC0B438ISfUOOCnpzQ+QpDHgOXB0iy' + \
       'CpXgAnJEUG4Jy7OgIIwDHgMoBLTrMC7BsBCOBttVrdb8650yOEAPi9Xu+UxXF8f' + \
       'oSQVNMGTAAfnXM3Pc+r+L5f9jyvAswBqxs2LwBTwI5kTAHdDf4KcB2YSGs4524A' + \
       'H4CKC8OwUSqVbm9+YADtdnt7v9+/45xbbjQaIax3b2CbpOPJXMABYFbSl801khY' + \
       '2m/sOJMWS4ry5v9a9/4P+YZCkrqRulr9lINYb4qSkvelCq9Xak3x+zgv61S96ET' + \
       'gHzEuaA6LBYKDEe5oXlHkiMwuAr8BF4D2wBlwDvplZmBfkZRmdTme1Vqs9iuPYB' + \
       '3YCA2DJzC4FQbCQF/Qd09KEuNw0COAAAAAASUVORK5CYII='

red = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+' + \
      'gvaeTAAABpklEQVRIie3WsWtTURTH8c99Bgtql6hVKYINriouFmy0WivFLv0nFG' + \
      'cRRBBsB1f/AxH/gSIOFoRqXlISqBYcdHMQLKJE1MFJGt5zsE9ibWxfbATB33Q55' + \
      '/7O954L93DJqZhqzLO8vkJeA0534RF1Y+pGG3bUoPiVycARHM7iMbMpr/Cyj7mT' + \
      'fPpdndApUaEcuIHxTRyohfmEW2PUNwWqsCfiTsrUBsU76X6LS+N87AiqcTThAQ5' + \
      '1Ccn0OjA1yotfQI8Z3MYiBv8Qkul9geEyb36AKhQCSzi2RZBMz1NOnKUVQcTlHk' + \
      'DgOC5CWO1mGft7AIJ3TQ5GgVM9hMCBfYxEuNBDCEiYjDCED4HrgdIutgdKuIq3b' + \
      'ftrgYmU/pT+wAQW2vLLKVdShtpqXEMzUFJlep7d653kETsr3KsyncXiNdO7wkzM' + \
      '3SV2rFejQTHmZu5riElj0ry+vza9/4P+YVDMQvzzO+kNyPeBWK4zkAVq7F1dftl' + \
      'KUB1WuF1noEExYQYCT/OCOv4ZnjAcUUXfmtQKzp3Jea0dOxpjMWE08BBNfEaccD' + \
      '4vBL4BC1BjXztbajkAAAAASUVORK5CYII='

green = 'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAABmJLR0QA/wD/AP+' + \
        'gvaeTAAABp0lEQVRIie3WwWpTQRTG8d9cgwW1m6hVKYItblXcWNBota0Uu+lLKK' + \
        '5FEEGwXbj1DUR8AREXCkI1NykJVAtd6M6FYBEloi5cScO9LtLEWBvbGxtB8FsN5' + \
        '8w5/znDzJkhq2IlsRdZw3KZQZzpIkbUTVA32riiqrxvpgRHcLhlj92Xeo1X+jx2' + \
        '0uffpQkdPUUFwQ1MbGJBdcxJ3DKmsjlQ0R6RO1LTGyTvpAfqLpnwqTOo7KjEQxz' + \
        'qEtLUG8G0US9/BT01aJsFDP4hpKkPckYUvP0BKsoJFnFsiyBNLUmdcE69cbwjl3' + \
        'sAgeO4CGG1mmXs7wEI3qs5GAlO9xACB+xzKsKFHkIaSkxFGMJHwXXBsF22C4ZxF' + \
        'e/appcFk1L9Uv2CScy3+ZelrkgNteW4hlpjXDJjzu51V/LETkX3lMy0bGu7d9Gs' + \
        '2F2LdqyboyovdjP7NsRSsTRr2F/r3v9B/zIoNi/+6Z70CNRoiAUVAy1L2d7V0de' + \
        'tBDWe5BW3VQyoykvMguB5VlDnP8MzIyIl9K3xrGDc2Wzb2rmiMQsSo4JHqOELYo' + \
        'nzWSHwHeCSY18iEoD8AAAAAElFTkSuQmCC'

try:
    status = loads(get('https://garoahc.appspot.com/status').content)['open']
    if status:
        img = green
    else:
        img = red
except ConnectionError:
    img = gray

print(f"|image={img} imageWidth=26, imageHeight=26")
print('---')
print('Visite nosso site | href=https://garoa.net.br')
print('Atualizar status | refresh=true')

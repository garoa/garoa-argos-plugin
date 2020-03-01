#!/usr/bin/env python3

# Umbrella icon by Icons8: https://icons8.com/icon/389/umbrella

# <bitbar.title>Garoa Hacker Clube Status</bitbar.title>
# <bitbar.version>v1.2</bitbar.version>
# <bitbar.author>Fabricio Biazzotto</bitbar.author>
# <bitbar.author.github>biazzotto</bitbar.author.github>
# <bitbar.desc>Exibe o status atualizado do Garoa Hacker Clube.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/OhCj6y1.png</bitbar.image>
# <bitbar.dependencies>python3,requests,json</bitbar.dependencies>

try:
    from requests import get
except ModuleNotFoundError:
    print('ERRO')
    print('---')
    print('Clique aqui para instalar `requests`|bash="sudo python3 -m pip '
          'install requests" terminal=true refresh=true')
from requests.exceptions import ConnectionError
from json import loads


gray = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+g' + \
       'vaeTAAABi0lEQVQ4jc2UsWvTURSFv3u1QoiLoZtE2qIUWghYXGymTEJrBUeXimP3' + \
       'QqAOOQmvdNVChrhUHToWl4JLIUOLf4AITk7VbBkUpMOPPIcmIm1SXkoHz/R499zv' + \
       '3MeDCwmStCPpTYr3eooJuJfow0YVWq3WRKfTeWhmszHGlwBmtmlmX3u93idJWRIw' + \
       'hHA7y7IN4Blwa0ReF9gFtiT9GAms1+svYoxNIHfRs/7Rb2BN0vvBxbXBQdIGsA1M' + \
       'JMLoe59WKpWTdrt99HdCSU+AD2cnHkPRzFZqtdq+SboBfAHuXhI20LdCoTDnZrZ8' + \
       'BTCAmW63+8hjjMtXABvosQPTwGt3L+Xz+ZvuvgA0gQw4NrNVdy8B88Bz4Hu/tg3c' + \
       '7/eUgFfADJLmhkU1Go1yCKEIIOmjpH2AEEJR0uKwnlGsYcZDSYcpXk8ijqH/H3hu' + \
       'fUl6wOmPLUn6OS5w2ISTQNnMyv0AB4qcbpjxgblc7gg4jjG+ldQEDoA7wN6lgNVq' + \
       '9Ze7LwGfgVVgyszWJb1LAf4BpclzdLyVffIAAAAASUVORK5CYII='

green = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+g' + \
        'vaeTAAABXklEQVQ4jdXTP2tUQRSG8d/cmIB/QbCLWxgUYcWFiCBmRY2NRdTeRklh' + \
        '4ScQ8gXsTBTTWBi1sLKwCdiod2RBC9uIlZXaRNIZFBaPhRsw7q65K9v4VMPMe57z' + \
        'NkMVSktK96pEt1USJocq5f4qfGvUVyeFw8J+ULqG98Jr09q9d//Jc+NGzOEy9vZZ' + \
        'tyZ5bMRNp3zuLyzNYhHb+zbfzLrkujMebVwUv8nmcH8AGewQHspubG6YXRKedjWu' + \
        'TvjhonOWkxVjVq3g4D/KNvhgXb2wamYIMpiw0/lCmBmC7BfhQiE5INyWNHy3S3JM' + \
        'WEQbH3FF0lA4IrmKT523O8JkZ6YhWZBM8Eq957YXmrIayJ4pLXfONdlUz5l+ri6y' + \
        'lqxVJVpsHRmM/1H40nFZyxt7hiNkn9D0TROEQqgJa1WE3X+3Zbe2dxjDE9RxVpg1' + \
        '7cHgQsiOYl44gS+Su067JYmthD8BML5Xrn1Fjy8AAAAASUVORK5CYII='

red = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAABmJLR0QA/wD/AP+g' + \
      'vaeTAAABY0lEQVQ4jdXUv2vTQRjH8ddd24C1FgS32qFBKVRaSXGxWXRy8MfuYung' + \
      '0LmD0H/AVQsuDv4anBxcCg6OAR2kuVgqmXRRxyxCKbT2HNKAtol+U7L4mY7nPs/7' + \
      'eY7n7iigxNMGj4t4h4uYcD4XNPYEfmCkxOWfTOMs1LkbabZ4d5W9bnnhcCAxEVjN' + \
      '3MbpHvVaeLnP/Xm+9wQmlvAIJ/52rN+0HVi+yItOIHYWDVbxpA8YjGaeJ+790WGD' + \
      'W5nXhzvuQzlzs8J62KK0yxbOHRPW0eeTzMRdrg8ABuVtrkVt4KB0I2Iq8zAyFxjD' + \
      'vPak9/AVdyJz+1wILOLbwd5aphIYO8h9kCnbYKZbqTrVTSYh8abBOmwyWWehW04v' + \
      '1hElaolaEW/8t6U//YfADS4lau8ZHwhwiDOojlKFTAztabeKAI+83SandviEUuBV' + \
      'bl+FK5mlCs+O07WPzCbeJn4kviRWcsGP4xczKFY6tfyQCAAAAABJRU5ErkJggg=='

try:
    status = loads(get('https://garoahc.appspot.com/status').content)['open']
    if status:
        img = green
    else:
        img = red
except ConnectionError:
    img = gray

print(f"|image={img}")
print('---')
print('Visite nosso site | href=https://garoa.net.br')
print('Atualizar status | refresh=true')
#!/usr/bin/env python3

# Umbrella icon by FontAwesome: https://fontawesome.com/icons/umbrella
# Creative Commons Attribution 4.0: https://fontawesome.com/license

# <bitbar.title>Garoa Hacker Clube Status</bitbar.title>
# <bitbar.version>v1.3</bitbar.version>
# <bitbar.author>Fabricio Biazzotto</bitbar.author>
# <bitbar.author.github>biazzotto</bitbar.author.github>
# <bitbar.desc>Exibe o status atualizado do Garoa Hacker Clube.</bitbar.desc>
# <bitbar.image>https://i.imgur.com/8nFc3VO.png</bitbar.image>
# <bitbar.dependencies>python3,requests</bitbar.dependencies>

try:
    from requests import get
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    print('ERRO')
    print('---')
    print('Clique aqui para instalar <tt>requests</tt>.|bash="sudo -H python3'
          ' -m pip install requests&&exit" terminal=true refresh=true')

from json import loads


gray = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAASCAYAAABb0P4QAAABkklEQVQ4y6WUu0ub' + \
       'YRSHn/dNQtpRa+jQC162LqW6dLAgdSkWl86CS4eCQgadHMIvAROHVsEbfIP/gAhF' + \
       'EAcXQXBw6aAgLraUBhLEIYKgX/iat8uHhGguTX7juTwv55z3HEMTeZ4XKxQKR0AF' + \
       'eCspaBRvm8GKxeIw8AYYMsa88zwv1ijHPGSUNAJMAR+BxzXuG2AHWJV00BCYzWYT' + \
       '5XJ5AxinNW0DnyVd3gNK6gf2gZf8n34D7yX9vAPmcrku3/d/AL20p1/AoKSSBfB9' + \
       'f6UDGEAfsAJgJL0CTppNvAU5a+1rG06zUxiAqVQqXywwBiwBiXg83g18q34VWACe' + \
       'AQngaw1kEXgCPAWWgbGotXYilUodVgXNSooCyRAwD3wP4Z+AMjAHLEmaqcpLZjKZ' + \
       'zXof+xGwFrajB/gTul4AF8A6MC3ptqVNqYE/rwZKyre9y+0oWm9i6XT6QyQSOQ2C' + \
       '4G/HQEmjzrndIAjOjTFrzjnC81VqBqxX8ll4VQacc4uhbU/SdVtASXljzDhwDFwB' + \
       'W8BkKyX/A8OHf+qE3/CsAAAAAElFTkSuQmCC'

green = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAASCAYAAABb0P4QAAABaUlEQVQ4y63UT0uU' + \
        'URTH8c+dcaSgTeXYwor+7NpEtglU9KlNFL4GNy2C6W0EEWWR6a530EaIFgrO47gS' + \
        'pEVBtNGIXIkLA6EWznNbzEPh6Pxx9Le6nHPP957DOecGnbSmZNeqIJO5I7HX7nqh' + \
        'C9goboluC8asKbULCYdaqyYEFTzE6Sbvb3wQvDWu1h5YU5Z5h0ndKJiXeSSxfRC4' + \
        '4pq6Ki47mn4oumvMxn/girPqPuGK3vRdNCyx02jKnpljwOCqYKaRYc0NmS8dO95Z' + \
        'UXCzIFM5AVgjuehxAQ/wSlRWdE70sunVZ/oMicqCF02Qaf3OK7mANw3WkpFD5vC1' + \
        'VJR6ruqM1KLUQn5+mvumD8QtGWk12KcEs6IKBgQ/83wvGbRlyxyeSPzpblP2wy/u' + \
        'AyY2e9/lHtTXcgCW3Vf3FfXjA1P3BB8VrWM2t2bY6QRsVfK3/Fe5zr9uLkjs9gZM' + \
        'bMpM4jN+4b2SqW5K/gs/n2H7bpiKpgAAAABJRU5ErkJggg=='

red = 'iVBORw0KGgoAAAANSUhEUgAAABQAAAASCAYAAABb0P4QAAABb0lEQVQ4y63UO2tU' + \
      'QRiA4WfGXVAIhKjBwgvG0iJr1EKIgpdGI/kNNhbC+jcEERNFjZ3/II0gIloIdkLY' + \
      'W4iFoEGSKggmNgpZz1gkyLKe7B43vuU3M+8w32WCPixQLvEe2TfOXaLda38sIDuP' + \
      'CZwZ4cIC5V5nQl6wzkVUA9exr2v5R+BF4Mk473oKa4xGnmFaAQLPN7l5lq9/CVuc' + \
      'SLxNHPNvfIlcHufzH2GLkYwajhuM5cTpCdYjZDzehQzGwpZDqHEystiv4gVIkUrc' + \
      'Q/U/yCAkbsXEFB60tyq8HzOdt+JuxuE2o4n7XZLZMgcCh/AoMaXOZE4fPmyQmtxb' + \
      'YqjJmwavlxiqc6dBajCbc24yt7GX2bvB3DDV7xxMrGy3xNESa5s8Heb2GD8LTUon' + \
      'TY50CiusDjzLg1DKrT9hkattPuDXroV1rkReBj4l5rbDWYn1AvO9Y94+dv00r05x' + \
      'rZ8wN4cVVgPTiRY2EvOBG0We/BtUr2OKb+a2RgAAAABJRU5ErkJggg=='

try:
    status = loads(get('https://garoa.net.br/status/spaceapi.json').text)['state']['open']
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

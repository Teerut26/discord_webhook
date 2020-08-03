import requests
import time
import random
import string
from datetime import datetime

def discord_send(word):
  url = "https://discordapp.com/api/webhooks/739512178729812059/T8wTP7Q1cRPVEjQ7qtxIh6lPzkwSKSjBtisqQ2sVwfzsfxQHbSFcRNRiAerIfL7_sHYD"

  payload = {'username': ''+str(word)+'',
  'avatar_url': 'https://conceptdraw.com/a1719c3/p1/preview/640/pict--wall-clock-time-vector-stencils-library',
  'content': ''+str(word)+''}
  files = [

  ]
  headers = {
    'Cookie': '__cfduid=dd7b87cb7fd3d396ff6f784f1213507391596383981; __cfruid=6493150f05011e749123f445366e11b6580742e7-1596383981'
  }

  response = requests.request("POST", url, headers=headers, data = payload, files = files)

  print('Status : OK_'+str(word))

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

for x in range(1000000):
  now = datetime.now()
  timestamp = datetime.timestamp(now)
  discord_send(datetime.fromtimestamp(timestamp)) 
  time.sleep(120)

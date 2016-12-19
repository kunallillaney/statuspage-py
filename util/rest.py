import requests
from settings import Settings
settings = Settings()

def getUrl(url):
  try:
    response = requests.get(url, headers={'Authorization': 'OAuth {}'.format(settings.API_TOKEN, verify=True)})
    return response
  except Exception as e:
    raise e

def postUrl(url, data):
  try:
    response = requests.post(url, json=data, headers={'Authorization': 'OAuth {}'.format(settings.API_TOKEN, verify=True)})
    return response
  except Exception as e:
    raise e

def patchUrl(url, data):
  try:
    response = requests.patch(url, json=data, headers={'Authorization': 'OAuth {}'.format(settings.API_TOKEN, verify=True)})
    return response
  except Exception as e:
    raise e

def deleteUrl(url):
  try:
    response = requests.delete(url, headers={'Authorization': 'OAuth {}'.format(settings.API_TOKEN, verify=True)})
    return response
  except Exception as e:
    raise e

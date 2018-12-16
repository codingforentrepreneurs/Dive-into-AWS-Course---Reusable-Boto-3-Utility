import requests
from main import AWS

botocfe = AWS()
key = 'files/screen_shot.png'
post_data = botocfe.presign_post_url(key=key)

file_path = 'screen.png'

with open(file_path, 'rb') as data:
    files = {'file': data}
    url = post_data['url']
    request_data = post_data['fields']
    r = requests.post(url, data=request_data, files=files)
    print(r.status_code) # range of 200 299, 204
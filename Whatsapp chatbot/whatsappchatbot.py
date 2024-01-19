import requests

url = "https://api.ultramsg.com/instance75165/instance/settings"

payload = "token=dkpxrprzvdqx4w4s&sendDelay=1&webhook_url=https://webhook.site/d3a674d0-3e53-40c2-a9a7-7f360c545147&webhook_message_received=&webhook_message_create=&webhook_message_ack=&webhook_message_download_media="
payload = payload.encode('utf8').decode('iso-8859-1')
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
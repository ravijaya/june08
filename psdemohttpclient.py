import requests
import re

requests.Request
url = 'https://google.com'
response = requests.get(url)

print(response.status_code)
print()
print(response.headers)
print()
print(response.content)
print()
print(response.text)

pattern = '<a .*? href="(.+?)">.*?</a>'

for m in re.finditer(pattern, response.text):
    print(m.group(), m.group(1))
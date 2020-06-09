info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info)
print()

value = info.pop('desc')
del info['domain']

print(value)
print(info)

# del info  # delete's the dict
# print(info)
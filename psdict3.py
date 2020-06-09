info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2
}

print(info)
print()

item = 'version'

print('app' in info)
exit(0)

if item in info:   # validate/search for the key
    info[item] = 3.6  # update

info['arch'] = 'x86_64'  # adding an element

print(info)

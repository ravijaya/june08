info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,
    'arch': ['x86_64', 'arm', 'sparc']
}

# iterate for its key => value pair

for key, value in info.items():
    if type(value) is list:
        print(key, '->')
        for item in value:
            print('\t', item)
    else:
        print(key, '->', value)

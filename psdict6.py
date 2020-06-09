info = {
    'host': 'ws1',
    'domain': 'rootcap.in',
    'desc': 'web server',
    'app': 'apache httpd',
    'version': 2.2,
    'arch': ['x86_64', 'arm', 'sparc']
}

print(info.keys())
print()
print(info.values())
print()
print(2.2 in info.values())  # for a value in the dict
print()
print(info.items())

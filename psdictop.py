from json import dumps

info = {
    'lang': 'perl',
    'author': {
        'first': 'larry',
        'last': 'wall'
    }
}

print(dumps(info, indent=2))

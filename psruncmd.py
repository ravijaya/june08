from subprocess import check_output
from sys import platform


if platform in ['linux', 'darwin']:
    cmd = ['curl', 'http://stash.compciv.org/ssa_baby_names/names.zip', '--output', 'names.zip']
elif platform == 'win32':
    cmd = ['ipconfig']
else:
    raise OSError(f'unsupported OS: {platform}')

op = check_output(cmd, stderr=open('/dev/null', 'w'))
print(op.decode())  # bytes into str


"""
ravi.goglobium@gmail.com

97909 16181
"""
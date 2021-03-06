"""single threaded ssh client"""

import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.password)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read()
        response = output if output else stderr.read()  # if else conditional operator  (? :)
        return response

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    from getpass import getpass

    # ssh = CustomSSHClient('127.0.0.1', 22, 'training', getpass('password for the user `training` :'))
    ssh = CustomSSHClient('127.0.0.1', 22, 'training', 'training')
    op = ssh.check_output('/sbin/ifconfig')
    print(op)
    print()
    print(type(op))
    print()
    print(op.decode())  # convert bytes into str

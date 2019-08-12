import paramiko
import sys


host = '192.168.1.3'
username = 'root'
password = 'nodeMachine'
command  = 'cat /etc/redhat-release'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,username=username,password=password)
print ("Connected To Host")

stdin_result , stdout_result , stderr_result = ssh.exec_command(command)
for result in stdout_result:
    print (result)

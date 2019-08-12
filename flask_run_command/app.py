from flask import Flask , render_template , request
import os
import paramiko

application = Flask(__name__)

@application.route('/')

def index():
    return render_template('index.html')

@application.route('/command_run',methods=['POST','GET'])
def command_run():
    if request.method == 'POST':
        host    = request.form['host']
        username= request.form['username']
        password= request.form['password']
        command = request.form['command']

        print(host)
        print(username)
        print(password)
        print(command)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,username=username,password=password)
        print("Connected to remote host {0}".format(host))

        stdin_result , stdout_result , stderr_result = ssh.exec_command(command)

        for result in stdout_result:
            print(result)

        return render_template("index.html")

if __name__ == '__main__':
    application.run(debug=True)


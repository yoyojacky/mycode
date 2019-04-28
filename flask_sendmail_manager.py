from flask import Flask, render_template
from flask_script import Manager
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_USERNAME'] = 'emailaddress'
app.config['MAIL_PASSWORD'] = 'passcode'
mail = Mail(app)
manager = Manager(app)

def async_send_mail(msg):
    with app.app_context():
        mail.send(msg)

# 封装发送邮件方法
def send_mail(subject, to):
    msg = Message(subject=subject, recipients=[to], sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('mail.html')
    t = Thread(target=async_send_mail, args=(msg,))
    t.start()
    return t

@app.route('/')
def index():
    send_mail('hello jacky', 'xxxx@163.com')
    return '邮件已经发送'

if __name__ == "__main__":
    manager.run()

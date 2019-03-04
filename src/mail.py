import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import SMTP, USERNAME, PASSWORD, RECEIVER

 
mail_host = SMTP
mail_user = USERNAME
mail_pass = PASSWORD 


def send_email(subject, content):
    ret = False
    sender = '%s@126.com' % USERNAME
    receivers = [RECEIVER]
    message = MIMEText(content, 'plain', 'utf-8')
    # from & to 必须和发送和接受的地址一样，不然会报554错误
    message['From'] = sender
    message['To'] = receivers[0]
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)
        # smtpObj.set_debuglevel(1)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
        smtpObj.quit()
        ret = True
    except smtplib.SMTPException as e:
        print ("Error: 无法发送邮件")
        print ("Error: %s", e)
    return ret


def main():
    subject = '会议纪要'
    content = 'we will meet tomorrow'
    send_email(subject, content)


if __name__ == "__main__":
    main()

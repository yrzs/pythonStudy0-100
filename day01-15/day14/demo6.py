from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender = '260652022@qq.com'
    receivers = [
        '1669616538@qq.com'
    ]
    message = MIMEText('用Python发送邮件的测试。', 'plain', 'utf-8')
    message['From'] = Header('月染指上', 'utf-8')
    message['To'] = Header('明智之举', 'utf-8')
    message['Subject'] = Header('测试邮件', 'utf-8')
    smpter = SMTP('smtp.qq.com')
    smpter.login(sender, 'juukhlmxocyibjhi')
    smpter.sendmail(sender, receivers, message.as_string())
    print("邮件发送完成！")


if __name__ == '__main__':
    main()

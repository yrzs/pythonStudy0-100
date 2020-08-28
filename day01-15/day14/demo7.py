from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    # 创建文本内容
    text_content = MIMEText('python 邮件测试', 'plain', 'utf-8')
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    message['Subject'] = Header("测试带附件的邮件")
    message['From'] = Header('你爹', 'utf-8')
    message['To'] = Header('有缘人', 'utf-8')
    # 将文本内容添加到邮件消息对象
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('img/post.jpg', 'rb') as f:
        img = MIMEText(f.read(), 'base64', 'utf-8')
        img['Context-Type'] = 'image/jpeg'
        img['Content-Disposition'] = 'attachment; filename=post.png'
        message.attach(img)

    # 创建邮件对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全连接
    smtper.starttls()
    sender = 'xx.qq.com'
    key = 'xxxxx'
    receivers = [
        'xx@qq.com',
        'xx@qq.com',
        'xx@qq.com'
    ]
    smtper.login(sender, key)
    smtper.sendmail(sender, receivers, message.as_string())
    smtper.quit()
    print("发送成功！")


if __name__ == '__main__':
    main()

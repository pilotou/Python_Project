import smtplib
from email.mime.text import MIMEText
# sending email to QQ
# email title

def sendEmail(exchange_rate: float):
    subject = "澳元汇率"
    sender = "######@163.com"
    content = f'Au to RMB exchange rate now is {exchange_rate}'


    recver = "#####@qq.com"
    password = "######"

    message = MIMEText(content, "plain", "utf-8")

    message['Subject'] = subject
    message['To'] = recver
    message['From'] = sender
    # initiate smtp server
    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
    # sender login
    smtp.login(sender, password)
    # encapsulate the message
    smtp.sendmail(sender, [recver], message.as_string())


import logging
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fname = "gcodeGenerator.log"
def enable_logging():

    logging.basicConfig(filename=fname, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def send_log_file():
    logging.shutdown()

    smtp_username = os.environ.get('SMTP_USERNAME')
    smtp_password = os.environ.get('SMTP_PASSWORD')

    smtp_server = 'smtp.ukr.net'
    smtp_port = 465  # Порт SSL

    # Заповнюємо дані листа
    sender_email = smtp_username
    receiver_email = 'denys.tovhin@hneu.net'
    subject = 'Лабораторна робота 1. Програмування інтернет'

    # Створюємо об'єкт листа
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Додаємо текстове повідомлення
    body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Простий HTML-документ</title>
</head>
<body>
    <h1>Hello, world!</h1>
    <p>Це <strong>простий</strong> HTML-документ з використанням кількох тегів.</p>
    <p>Використаємо різні теги, такі як <em>параграфи</em>, <strong>сильні</strong> і <em>курсивні</em> написи.</p>
    <p>Команда 2: Товгін, Ткалін, Гончаров!</p>
</body>
</html>
"""
    msg.attach(MIMEText(body, 'html'))

    # Додаємо файл до листа
    filename = fname
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    # Надсилаємо лист
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print("Помилка відправлення листа:", e)
    finally:
        server.quit()
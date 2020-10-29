from dotenv import load_dotenv
load_dotenv()

import smtplib, ssl
from email.message import EmailMessage
from email.utils import make_msgid
from email.iterators import _structure
import pyqrcode
import io, json, os, csv
from jinja2 import FileSystemLoader, Environment
import logging

fileloader = FileSystemLoader('templates')
j_env = Environment(loader=fileloader)

template = j_env.get_template('temp.html')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('tests.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

def get_customized_email(user_data, subject, email_from):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = email_from
    message['To'] = user_data['Email']
    message.set_content(f'''\
        This email contain HTML contents.Please try a HTML capable email reader
        ''')

    asparagus_cid = make_msgid()
    html = template.render(data=user_data, asparagus_cid=asparagus_cid[1:-1])
    message.add_alternative(html, subtype='html')

    user_qrcode = get_QR(user_data)

    message.get_payload()[1].add_related(user_qrcode.getvalue(), 'image', 'png', cid=asparagus_cid)

    return message


def get_QR(raw_data, scale=6):
    buffer = io.BytesIO()
    data = json.dumps(raw_data)

    qr = pyqrcode.create(data, error='M', mode='binary')
    qr.png(buffer, scale=scale)

    return buffer


if __name__ == '__main__':
    my_address = os.environ.get('TEST-EMAIL')
    password = os.environ.get('TEST-EMAIL-PASS')
    smtp_sever = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_sever, port, context=context) as server:
        server.login(my_address, password)
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)

            headers = next(reader)
            subject = 'This is a test email'
            for row in reader:
                data = {}
                for key, value in zip(headers, row):
                    data[key] = value

                message = get_customized_email(data, subject, my_address)
                try:
                    server.sendmail(my_address, data['Email'], message.as_string())
                    logger.info(f"Email successfully delivered to {data['Email']}")
                except smtplib.SMTPException:
                    logger.error(f"Email failed to deliver at {data['Email']}")
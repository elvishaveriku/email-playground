import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Elvis'
email['to'] = 'elvisfatmir1@gmail.com'
email['subject'] = 'You are the winner!'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('elvispython@gmail.com', 'jneg zraz gbje gslq')
    smtp.send_message(email)
    print('all good boss!')

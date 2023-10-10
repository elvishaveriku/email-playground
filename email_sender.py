import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Elvis'
email['to'] = 'hatixhekercuku1@gmail.com'
email['subject'] = 'Excuse me boss, you have a text message!'

email.set_content('Hi there')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('elvispython@gmail.com', 'jneg zraz gbje gslq')
    smtp.send_message(email)
    print('all good boss!')


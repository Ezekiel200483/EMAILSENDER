import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Olopade Ezekiel'
email['to'] = 'ezekielolopade9999@gmail.com'
email['subject'] = 'Urgency!!'

email.set_content('I am a python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('olopade.ezekiel1998@gmail.com','Olopade_200483.')
    smtp.send_message(email)
    print('all good boss!')



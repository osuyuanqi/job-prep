'''
email: hope it helps in the future

parameters:
 @from: yuanqingxiao@gmail.com
 @to: Raymond Yuan
 @html: index.html is the content,$->replace with dict
 @subject: title
note: 
https://security.google.com/settings/security/apppasswords
'''
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


your_email,pwd = '',''

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Raymond Yuan'
email['to'] = 'yuanqingxiao@outlook.com,yuanqi@oregonstate.edu'
email['subject'] = 'tst message'
email.set_content(html.substitute({'name': 'Raymond','language': 'Python'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(your_email, pwd)
  smtp.send_message(email)
  print('done!')

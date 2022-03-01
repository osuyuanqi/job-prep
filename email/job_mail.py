'''
email: ask for referal, personalize->introduction.html, pdf attached

parameters:
 @need to set: candidate,referral part
 @from: your_email@gmail.com
 @to: referral's name
 @html: index.html is the content,$->replace with dict
'''
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

# candidate part: non-empty part can't set to '' or None
candidate,your_email,pwd,LinkedIn,conact_number,resume = 'your_name','your_email@gmail.com','your_pwd','','','resume.pdf'

# referral part
referral,ref_email,company_name,job_position,intr_module ='referral_name','referral@email_address.com','','','index.html'
job_link1,job_name1 = '',''
job_link2,job_name2 = '',''
job_link3,job_name3 = '',''

# program begin
html = Template(Path(intr_module).read_text())
email = EmailMessage()
email['from'] = candidate
email['to'] = ref_email
email['subject'] = '[Ask for Referral] [' + candidate + '] [' + company_name + '] [' +job_position + ']'
email.set_content(html.substitute({'referral': referral,'company_name': company_name,'job_position':job_position,'candidate':candidate,'LinkedIn':LinkedIn,'your_email':your_email,'con_num':conact_number,'job_link1':job_link1,'job_link2':job_link2,'job_link3':job_link3,'job_name1':job_name1,'job_name2':job_name2,'job_name3':job_name3}), 'html')

files = [resume]

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(your_email, pwd)
  smtp.send_message(email)
  print('done!')

from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'jay.aby.codes@gmail.com'
email_password = 'hktxiyjefjdefnky'
email_receiver = 'joelabiola04@gmail.com'

subject = 'check out my codes'
body = """
Code siri nice
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP('smtp.gmail.com', 465) as smtp:
    smtp.starttls(context=context)
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

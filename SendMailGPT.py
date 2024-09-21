import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date


def send_email(subject, body, to_email, sender_email, sender_password):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Establish a connection to the Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        # Enable TLS encryption
        server.starttls()

        # Log in to the Gmail SMTP server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())


# Set your Gmail credentials
subject = "Savings Confirmation"
current_date = date.today()
body = "Hi, you have saved money on this day: {}".format(current_date)
to_email = "joelabiola04@gmail.com"
sender_email = "jay.aby.codes@gmail.com"
sender_password = "hktxiyjefjdefnky"

# Send the email
send_email(subject, body, to_email, sender_email, sender_password)

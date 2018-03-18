import smtplib
from email.mime.text import MIMEText
from config import username, password


def send_mail(recipients, content):
    COMMASPACE = ', '
    msg = MIMEText(content)
    msg['Subject'] = 'Free shit on humblebundle right now!'
    msg['From'] = 'Be Humble'
    msg['Bcc'] = COMMASPACE.join(recipients)

    # Send the email via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(username, password)
    s.send_message(msg)
    s.quit()

import smtplib
from mail.mailer_config import default_config, text
from utils.code_generator import generate_code
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from models.nova_user import get_email


def send_auth_code(user_id: int):
    # Logs in with credentials
    server = smtplib.SMTP(default_config['smtp'], default_config['port'])
    server.ehlo()
    server.starttls()
    server.login(default_config['email'], default_config['password'])

    # Prepares the email
    me = default_config['email']
    you = get_email(user_id)
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Nova Bl4ack code verification'
    message['From'] = me
    message['To'] = you

    # Unique and personal code
    code = generate_code()
    content = MIMEText(text.format(code), 'html')
    message.attach(content)
    # Sends the email
    problems = server.sendmail(me, you, message.as_string())
    server.quit()
    # Returns the code for checking if correct later
    return code


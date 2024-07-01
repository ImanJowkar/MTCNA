from decouple import config
import smtplib, ssl
from email.message import EmailMessage

FROM=config('FROM')
TO=config('TO')
SMTP_HOST=config('SMTP_HOST')
SMTP_APIKEY=config('SMTP_APIKEY')
SMTP_PORT=config('SMTP_PORT')




def send_smtp_email(subject, time_chris, body, backup_file):
    text = f"""
    <h1> hello Iman, I hope you are good.</h1>
    <h3>{time_chris}</h3>
    <pre id="json">{body}</pre>


    """
    msg = EmailMessage()
    msg.set_content(text, subtype='html')
    msg["Subject"] = subject
    msg["From"] = FROM
    msg["To"] = TO

    with open(backup_file, 'rb') as file:
        file_data = file.read()
        file_name = 'backup-file'
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    context=ssl.create_default_context()

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], SMTP_APIKEY)
        smtp.send_message(msg)
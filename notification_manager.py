import smtplib
from twilio.rest import Client
from config import Config

EMAIL = Config.EMAIL
PASSWORD = Config.PASSWORD
MAIL_PROVIDER_SMTP_ADDRESS = Config.MAIL_PROVIDER_SMTP_ADDRESS
TWILIO_SID = Config.TWILIO_SID
TWILIO_AUTHENTICATION_TOKEN = Config.TWILIO_AUTHENTICATION_TOKEN
TWILIO_VIRTUAL_NUMBER = Config.TWILIO_VIRTUAL_NUMBER
TWILIO_VERIFIED_NUMBER = Config.TWILIO_VERIFIED_NUMBER


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTHENTICATION_TOKEN)

    def send_emails(self, emails, email_message, link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for email_add in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email_add,
                    msg=f"Subject:Amazing Flight Deal!\n\n{email_message}\n{link}".encode('utf-8')
                )

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

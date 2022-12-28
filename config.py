from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """Set configuration vars from .env file"""

    TEQUILA_API_ENDPOINT = os.getenv("TEQUILA_API_ENDPOINT")
    TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
    SHEETY_API_ENDPOINT = os.getenv("SHEETY_API_ENDPOINT")
    MAIL_PROVIDER_SMTP_ADDRESS = os.getenv("MAIL_PROVIDER_SMTP_ADDRESS")
    TWILIO_SID = os.getenv("TWILIO_SID")
    TWILIO_AUTHENTICATION_TOKEN = os.getenv("TWILIO_AUTHENTICATION_TOKEN")
    TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
    TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

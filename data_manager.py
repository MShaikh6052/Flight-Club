import requests
from config import Config

SHEETY_API_ENDPOINT = Config.SHEETY_API_ENDPOINT


class DataManager:

    def get_data(self):
        response = requests.get(f"{SHEETY_API_ENDPOINT}/prices")
        return response.json()["prices"]

    def add_codes(self, codes):
        for place in codes:
            update = {
                "price": {
                    "iataCode": place
                }
            }
            requests.put(
                url=f"{SHEETY_API_ENDPOINT}/prices/{codes.index(place)+2}",
                json=update
            )

    def get_emails(self):
        response = requests.get(f"{SHEETY_API_ENDPOINT}/users")
        return response.json()["users"]

import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from config import Config

TEQUILA_API_ENDPOINT = Config.TEQUILA_API_ENDPOINT
TEQUILA_API_KEY = Config.TEQUILA_API_KEY


class FlightSearch:

    def flight_checker(self, original, destination):
        next_day = datetime.now() + timedelta(days=1)
        six_months_later = datetime.now() + timedelta(days=180)
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        flight_parameters = {
            "fly_from": original,
            "fly_to": destination,
            "date_from": next_day.strftime("%d/%m/%Y"),
            "date_to": six_months_later.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "CAD",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(
            url=f"{TEQUILA_API_ENDPOINT}/v2/search",
            params=flight_parameters,
            headers=headers
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            flight_parameters["max_stopovers"] = 1

            response = requests.get(
                url=f"{TEQUILA_API_ENDPOINT}/v2/search",
                params=flight_parameters,
                headers=headers
            )

            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                route = data["route"]

                flight_data = FlightData(
                    price=data["price"],
                    o_city=route[0]["cityFrom"],
                    o_airport=route[0]["flyFrom"],
                    d_city=route[1]["cityTo"],
                    d_airport=route[1]["flyTo"],
                    departure_date=route[0]["local_departure"].split("T")[0],
                    arrival_date=route[2]["local_departure"].split("T")[0],
                    stopovers=1,
                    by_city=route[0]["cityTo"]
                )

                return flight_data

        else:
            route = data["route"]
            flight_data = FlightData(
                price=data["price"],
                o_city=route[0]["cityFrom"],
                o_airport=route[0]["flyFrom"],
                d_city=route[0]["cityTo"],
                d_airport=route[0]["flyTo"],
                departure_date=route[0]["local_departure"].split("T")[0],
                arrival_date=route[1]["local_departure"].split("T")[0],
                stopovers=0,
                by_city=""
            )

            return flight_data

    def get_codes(self, city):
        location_parameters = {
            "term": city,
            "location_types": "city"
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        response = requests.get(
            url=f"{TEQUILA_API_ENDPOINT}/locations/query",
            params=location_parameters,
            headers=headers
        )
        d_code = response.json()["locations"][0]["code"]
        return d_code

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()


if sheet_data[0]["iataCode"] == '':

    cities = [i["city"] for i in sheet_data]
    city_codes = [flight_search.get_codes(i) for i in cities]
    data_manager.add_codes(city_codes)

    sheet_data = data_manager.get_data()


locations = {
    data["iataCode"]: {
        "id": data["id"], "city": data["city"], "price": data["lowestPrice"]
    } for data in sheet_data
}

for l_code in locations:
    flight = flight_search.flight_checker(
        "YTO",
        l_code,
    )

    if flight is None:
        continue

    if locations[l_code]["price"] > flight.price:

        emails = data_manager.get_emails()

        email_list = [i["email"] for i in emails]
        name_list = [i["firstName"] for i in emails]

        message = f"Amazing Deal! Pay only ${flight.price} to fly from " \
                  f"{flight.o_city}-{flight.o_airport} to {flight.d_city}-{flight.d_airport}, " \
                  f"from {flight.departure_date} to {flight.arrival_date}!"

        if flight.stopovers != 0:
            message = message + f"\nFlight has {flight.stopovers} stopover by {flight.by_city}."

        flight_link = f"https://www.google.com/flights?hl=en#flt={flight.o_airport}.{flight.d_airport}." \
                      f"{flight.departure_date}*{flight.d_airport}.{flight.o_airport}.{flight.arrival_date}"

        notification_manager.send_emails(email_list, message, flight_link)
        # notification_manager.send_sms(message+flight_link)

class FlightData:

    def __init__(self, price, o_city, o_airport, d_city, d_airport, departure_date,
                 arrival_date, stopovers, by_city):
        self.price = price
        self.o_city = o_city
        self.o_airport = o_airport
        self.d_city = d_city
        self.d_airport = d_airport
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.stopovers = stopovers
        self.by_city = by_city

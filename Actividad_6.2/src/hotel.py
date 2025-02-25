"""
This is the hotel class file
"""


class Hotel():
    """
    Basic attributes that represent the hotel
    """
    def __init__(
            self,
            hotel_id: str,
            name: str,
            location: str,
            rooms_total: int,
            price_per_night: float,
            rating: float
    ):

        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_total = rooms_total
        self.rooms_available = rooms_total
        self.price_per_night = price_per_night
        self.rating = rating

    def to_dict(self):
        """
        Converts to a dictionary for saving the file
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms_total": self.rooms_total,
            "rooms_available": self.rooms_available,
            "price_per_night": self.price_per_night,
            "rating": self.rating
        }

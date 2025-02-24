class Reservation():
    """
    Basic attributes that represent the hotel
    """
    def __init__(self, hotel_id : str, client_id : str, reservation_id : str, status : str):
        self.hotel_id = hotel_id
        self.client_id = client_id
        self.reservation_id = reservation_id
        self.status = status

    def to_dict(self):
        """
        Converts to a dictionary for saving the file
        """
        return {
            "hotel_id" : self.hotel_id,
            "client_id" : self.client_id,
            "reservation_id" : self.reservation_id,
            "status" : self.status
        }
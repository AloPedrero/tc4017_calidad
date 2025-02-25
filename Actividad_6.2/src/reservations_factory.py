"""
"""

from utils import *
from reservations import Reservation
import pandas as pd
import uuid

class ReservationFactory():
    @staticmethod
    def create_reservation(hotel_id : str,
                           customer_id : str):
        """
        This method opens teh reservations files and creates
        the reservation with hotel and client id, changes the 
        status
        """

        try:
            df = open_file("reservations.json", "reservations")
            
            if not check_if_id_exists("hotel", hotel_id) or not check_if_id_exists("customer", customer_id):
                raise Exception(f"Error: A hotel/client with ID does not exists.")   

            reservation_id = str(uuid.uuid4())
            reservation = Reservation(hotel_id, customer_id, reservation_id, "Reserved")

            df = pd.concat([df, pd.DataFrame([reservation.to_dict()])], ignore_index=True)

            save_file(df, "reservations.json")

            print(f"Reservation {reservation_id} created successfully!")

            return reservation

        except Exception as e:
            print(f"An error occured: {e}")
            return None
        
    @staticmethod
    def cancel_reservation(reservation_id : str):
        """
        This method opens the reservations files and creates
        the reservation with hotel and client id, changes the 
        status
        """
        
        try:
            df = open_file("reservations.json", "reservations")

            if not check_if_id_exists("reservation", reservation_id):
                raise Exception(f"Error: A reservation with ID {reservation_id} do not exists.")
            
            df.loc[df.reservation_id == reservation_id, "status"] = "Canceled"

            save_file(df, "reservations.json")
            print(f"Reservation {reservation_id} canceled successfully!")

            return True
        except Exception as e:
            print(f"An error occured: {e}")
            return False

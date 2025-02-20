"""
This is the activity 6.2 of unit testing
Alonso Pedrero Martinez
A01769076
"""

import pandas as pd
import pathlib
import sys
from customer import Customer
from customer_factory import CustomerFactory
from hotel import Hotel
from hotel_factory import HotelFactory


"""database = sys.argv[1]
function = sys.argv[2]"""

HotelFactory.create_hotel("1", "New ONE", "MX", 30, 305.0, 5.0)

HotelFactory.delete_hotel("1", "New ONE", "MX", 30, 305.0, 5.0)

HotelFactory.create_hotel("2", "New Holiday Inn", "MX", 30, 305.0, 5.0)


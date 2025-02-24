"""
This is the activity 6.2 of unit testing
Alonso Pedrero Martinez
A01769076
"""

import unittest
from customer_factory_test import CustomerFactoryTest
from hotel_factory_test import HotelFactoryTest
from reservations_factory_test import ReservationFactoryTest

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(CustomerFactoryTest))
    suite.addTest(unittest.makeSuite(HotelFactoryTest))
    suite.addTest(unittest.makeSuite(ReservationFactoryTest))

    runner = unittest.TextTestRunner()
    runner.run(suite)

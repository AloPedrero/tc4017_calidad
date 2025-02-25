from utils import *
import unittest
import uuid
from reservations_factory import ReservationFactory
from hotel_factory import HotelFactory
from customer_factory import CustomerFactory

class ReservationFactoryTest(unittest.TestCase):
    mock_hotel_id = None
    mock_customer_id = None

    @classmethod
    def setUp(cls):
        cls.mock_hotel_id = str(uuid.uuid4())
        cls.mock_customer_id = str(uuid.uuid4())

    @classmethod
    def tearDown(cls):
        HotelFactory.delete_hotel(cls.mock_hotel_id)
        CustomerFactory.delete_customer(cls.mock_customer_id)
        cls.mock_hotel_id = None
        cls.mock_customer_id = None


    def test_reservation_creation(self):

        hotel = HotelFactory.create_hotel(self.mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        self.assertIsNotNone(hotel)

        customer = CustomerFactory.create_customer(self.mock_customer_id, "John", "a@gmail.com", 722)
        self.assertIsNotNone(customer)

        reservation = ReservationFactory.create_reservation(self.mock_hotel_id, self.mock_customer_id)
        self.assertIsNotNone(reservation)

        df = open_file("reservations.json", "reservations")
        df_filtered = df.loc[(df["reservation_id"] == reservation.reservation_id)]
        status_values = df_filtered["status"].to_list()
        self.assertEqual(status_values[0], "Reserved")

    def test_reservation_cancelation(self):

        hotel = HotelFactory.create_hotel(self.mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        self.assertIsNotNone(hotel)

        customer = CustomerFactory.create_customer(self.mock_customer_id, "John", "a@gmail.com", 722)
        self.assertIsNotNone(customer)

        reservation = ReservationFactory.create_reservation(self.mock_hotel_id, self.mock_customer_id)
        reservation_canceled_succesfully = ReservationFactory.cancel_reservation(reservation.reservation_id)
        self.assertTrue(reservation_canceled_succesfully)

        df = open_file("reservations.json", "reservations")
        df_filtered = df.loc[(df["reservation_id"] == reservation.reservation_id)]
        status_values = df_filtered["status"].to_list()
        self.assertEqual(status_values[0], "Canceled")

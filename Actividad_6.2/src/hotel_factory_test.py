import unittest
import uuid
from hotel_factory import HotelFactory


class HotelFactoryTest(unittest.TestCase):

    def test_hotel_creation(self):
        mock_hotel_id = str(uuid.uuid4())
        hotel = HotelFactory.create_hotel(mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel.hotel_id, mock_hotel_id)
        self.assertEqual(hotel.name, "Holiday Inn")
        self.assertEqual(hotel.location, "MEX")
        self.assertEqual(hotel.rooms_total, 30)
        self.assertEqual(hotel.price_per_night, 500.0)
        self.assertEqual(hotel.rating, 5.0)

    def test_hotel_creation_failure(self):
        mock_hotel_id = uuid.uuid4()
        hotel = HotelFactory.create_hotel(mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        self.assertIsNone(hotel)

    def test_hotel_delete(self):
        HotelFactory.create_hotel("1616", "Holiday Inn", "MEX", 30, 500.0, 5.0)
        self.assertTrue(HotelFactory.delete_hotel("1616"))

    def test_hotel_delete_failure(self):
        self.assertFalse(HotelFactory.delete_hotel("NA"))

    def test_display_not_error(self):
        mock_hotel_id = str(uuid.uuid4())
        HotelFactory.create_hotel(mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        try:
            HotelFactory.display_hotel_info(mock_hotel_id)
        except Exception:
            self.fail("Failed to print the hotel information")
        HotelFactory.delete_hotel(mock_hotel_id)

    def test_display_failure(self):
        mock_hotel_id = str(uuid.uuid4())
        try:
            HotelFactory.display_hotel_info(mock_hotel_id)
            self.fail("The hotel information was displayed")
        except Exception:
            pass

    def test_modify_customer(self):
        mock_hotel_id = str(uuid.uuid4())
        original_hotel = HotelFactory.create_hotel(mock_hotel_id, "Holiday Inn", "MEX", 30, 500.0, 5.0)
        changed_hotel = HotelFactory.modify_hotel_info(mock_hotel_id, name = "ONE")
        self.assertNotEqual(original_hotel, changed_hotel)
        HotelFactory.delete_hotel(mock_hotel_id)

    def test_modify_customer_failure(self):
        mock_hotel_id = str(uuid.uuid4())
        self.assertIsNone(HotelFactory.modify_hotel_info(mock_hotel_id, name = "ONE"))
        

if __name__ == '__main__':
    unittest.main()
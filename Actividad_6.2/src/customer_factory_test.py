import unittest
import uuid
from customer_factory import CustomerFactory


class CustomerTest(unittest.TestCase):

    def test_customer_creation(self):
        mock_customer_id = str(uuid.uuid4())
        customer = CustomerFactory.create_customer(mock_customer_id, "John", "a@gmail.com", 722)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.customer_id, mock_customer_id)
        self.assertEqual(customer.name, "John")
        self.assertEqual(customer.email, "a@gmail.com")
        self.assertEqual(customer.phone, 722)

    def test_customer_creation_failure(self):
        mock_customer_id = uuid.uuid4()
        customer = CustomerFactory.create_customer(mock_customer_id, "John", "a@gmail.com", 722)
        self.assertIsNone(customer)

    def test_customer_delete(self):
        CustomerFactory.create_customer("1616", "John", "a@gmail.com", 722)
        self.assertTrue(CustomerFactory.delete_customer("1616"))

    def test_customer_delete_failure(self):
        self.assertFalse(CustomerFactory.delete_customer("NA"))

    def test_display_not_error(self):
        mock_customer_id = str(uuid.uuid4())
        CustomerFactory.create_customer(mock_customer_id, "John", "a@gmail.com", 722)
        try:
            CustomerFactory.display_customer_info(mock_customer_id)
        except Exception:
            self.fail("Failed to print the customer information")
        CustomerFactory.delete_customer(mock_customer_id)

    def test_display_failure(self):
        mock_customer_id = str(uuid.uuid4())
        try:
            CustomerFactory.display_customer_info(mock_customer_id)
            self.fail("The customer information was displayed")
        except Exception:
            pass

    def test_modify_customer(self):
        mock_customer_id = str(uuid.uuid4())
        original_customer = CustomerFactory.create_customer(mock_customer_id, "John", "a@gmail.com", 722)
        changed_customer = CustomerFactory.modify_customer_info(mock_customer_id, name = "Carlos Name")
        self.assertNotEqual(original_customer, changed_customer)
        CustomerFactory.delete_customer(mock_customer_id)

    def test_modify_customer_failure(self):
        mock_customer_id = str(uuid.uuid4())
        self.assertIsNone(CustomerFactory.modify_customer_info(mock_customer_id, name = "Carlos Name"))
        

if __name__ == '__main__':
    unittest.main()
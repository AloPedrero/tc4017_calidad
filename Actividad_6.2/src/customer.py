class Customer():
    """
    Basic attributes that represent the hotel
    """
    def __init__(self, customer_id: str, name: str, email: str, phone: int):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Convierte el hotel a un diccionario para guardarlo en JSON.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }
from utils import *
from customer import Customer
import pandas as pd

class CustomerFactory():
    """
    
    """
    @staticmethod
    def create_customer(customer_id: str,
                        name: str,
                        email: str,
                        phone: int):
        """
        This method opens the hotel files and adds the 
        """
        try:
            df = open_file("customers.json", "customer")
            
            if customer_id in df["customer_id"].astype(str).values:
                raise Exception(f"Error: A client with ID {customer_id} already exists.")

            client = Customer(customer_id, name, email, phone)


            df = pd.concat([df, pd.DataFrame([client.to_dict()])], ignore_index=True)
            

            save_file(df, "customers.json")

            print(f"Client {name} created successfully!")
            
            return client
        
        except Exception as e:
            print(f"An error occured while saving the customer: {e}")
            return None
    
    @staticmethod
    def delete_customer(customer_id: str):
        """
        
        """
        try:
            df = open_file("customers.json", "customer")

            empty_check(df)
            
            parse_to(df, "customer_id", str)

            mask = (df["customer_id"] == customer_id)

            if df.loc[mask].empty:
                raise Exception(f"Error: No customer found with the given attributes.")
        
            df = df.loc[~mask]

            save_file(df, "customers.json")
            print(f"customer '{customer_id}' deleted successfully.")
            
            return True
        
        except Exception as e:
            print(f"An error occured while deleting the customer: {e}")
            return False


    @staticmethod
    def display_customer_info(customer_id : str):
        """
        
        """
        df = open_file("customers.json", "customer")
        empty_check(df)

        parse_to(df, "customer_id", str)

        df_filtered = df.loc[(df["customer_id"] == customer_id)]
        
        print(df_filtered)

    @staticmethod
    def modify_customer_info(customer_id: str, **kwargs):
        """
        
        """
        try:
            df = open_file("customers.json", "customer")
            empty_check(df)

            parse_to(df, "customer_id", str)

            if customer_id not in df["customer_id"].values:
                raise Exception(f"Error: No customer found with ID '{customer_id}'.")

            valid_columns = ["name", "email", "phone"]

            for key, value in kwargs.items():
                if key in valid_columns:
                    df.loc[df["customer_id"] == customer_id, key] = value
                else:
                    print(f"Warning: '{key}' is not a valid attribute.")            
            
            customer_df = df.loc[df["customer_id"] == customer_id]

            modified_customer = Customer(
                customer_df["customer_id"],
                customer_df["name"],
                customer_id["email"],
                customer_id["phone"]
            )
        
            save_file(df, "customers.json")
            print(f"Customer '{customer_id}' updated successfully.")

            return modified_customer
        
        except Exception as e:
            print(f"An error occured while modifying the customer: {e}")
            return None

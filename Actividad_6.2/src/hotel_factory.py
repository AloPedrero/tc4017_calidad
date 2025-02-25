from utils import *
from hotel import Hotel
import pandas as pd


class HotelFactory():
    @staticmethod
    def create_hotel(hotel_id: str,
                     name: str,
                     location: str,
                     rooms_total: int,
                     price_per_night: float,
                     rating: float):
        """
        This method opens the hotel files and adds the 
        """
        try:
            df = open_file("hotels.json", "hotel")

            if hotel_id in df["hotel_id"].astype(str).values:
                raise Exception(f"Error: A hotel with ID {hotel_id} already exists.")
                

            hotel = Hotel(hotel_id, name, location, rooms_total, price_per_night, rating)

            df = pd.concat([df, pd.DataFrame([hotel.to_dict()])], ignore_index=True)

            save_file(df, "hotels.json")

            print(f"Hotel {name} created successfully!")
            
            return hotel
        
        except Exception as e:
            print(f"An error occured while saving the customer: {e}")
            return None

    
    @staticmethod
    def delete_hotel(hotel_id: str):
        """
        
        """
        try:
            df = open_file("hotels.json", "hotel")

            empty_check(df)
            
            parse_to(df, "hotel_id", str)

            mask = ((df["hotel_id"] == hotel_id))

            if df.loc[mask].empty:
                raise Exception(f"Error: No hotel found with the given attributes.")
        
            df = df.loc[~mask]

            save_file(df, "hotels.json")
            print(f"Hotel '{hotel_id}' deleted successfully.")
            
            return True

        except Exception as e:
            print(f"An error occured while deleting the hotel: {e}")
            return False

    @staticmethod
    def display_hotel_info(hotel_id : str):
        """
        
        """
        df = open_file("hotels.json", "hotel")
        empty_check(df)

        parse_to(df, "hotel_id", str)

        df_filtered = df.loc[(df["hotel_id"] == hotel_id)]
        
        print(df_filtered)

    @staticmethod
    def modify_hotel_info(hotel_id: str, **kwargs):
        """
        
        """
        try:
            df = open_file("hotels.json", "hotel")
            empty_check(df)

            parse_to(df, "hotel_id", str)

            if hotel_id not in df["hotel_id"].values:
                raise Exception(f"Error: No hotel found with ID '{hotel_id}'.")

            valid_columns = ["name", "location", "rooms_total", "price_per_night", "rating"]

            for key, value in kwargs.items():
                if key in valid_columns:
                    df.loc[df["hotel_id"] == hotel_id, key] = value
                else:
                    print(f"Warning: '{key}' is not a valid attribute.")

            hotel_df = df.loc[df["hotel_id"] == hotel_id]

            modified_hotel = Hotel(
                hotel_df["hotel_id"],
                hotel_df["name"],
                hotel_df["location"],
                hotel_df["rooms_total"],
                hotel_df["price_per_night"],
                hotel_df["rating"]
            )
        
            save_file(df, "hotels.json")
            print(f"Customer '{hotel_id}' updated successfully.")

            return modified_hotel
        
        except Exception as e:
            print(f"An error occured while modifying the hotel: {e}")
            return None
        


"""

"""
import pandas as pd
import pathlib
import sys
import time

start_time = time.time()
file_catalog = sys.argv[1]
file_order = sys.argv[2]


def file_management_existence(file_catalog_input):
    """
    This function checks if the file exists.
    """
    if not pathlib.Path(file_catalog_input).is_file():
        raise FileNotFoundError("File not found: ", file_catalog_input)

    print("Found file:", file_catalog_input)


def read_product_list(file_catalog_input):
    """
    This function opens the json file for the catalog.
    """
    file_management_existence(file_catalog_input)
    catalog = pd.read_json(file_catalog_input)
    return catalog


def read_sales_records(file_order_input):
    """
    This function opens the json file for the orders.
    """
    file_management_existence(file_order_input)
    order = pd.read_json(file_order_input)
    return order


def sales_result_decorator(order_input, catalog_input):
    """
    This function calculates the total cost for the items and the
    final total cost.
    """
    result = pd.merge(order_input,
                      catalog_input,
                      left_on="Product",
                      right_on="title",
                      how="inner")
    result["total_price"] = result["Quantity"] * result["price"]
    final_total_quantity = result["total_price"].sum()
    return final_total_quantity


def sales_result_export(final_sales_input):
    """
    This function exports the code to a .xtx file.
    """
    EXPORT_PATH = "../outputs/SalesResults.txt"

    with open(EXPORT_PATH, "a", encoding="UTF-8") as file:
        file.write("\n\n" + file_order + "\n\n")
        file.write(f"Time elapsed: {elapsed_time:.4f} seconds \n")
        file.write(f"total cost {final_sales_input}")

    print(f"Data successfully saved to {EXPORT_PATH}")
    print(f"Time elapsed for execution {elapsed_time:.4f} seconds")


catalog_file = read_product_list(file_catalog)
order_file = read_sales_records(file_order)
final_sales_quanity = sales_result_decorator(order_file, catalog_file)
print("Final price:", final_sales_quanity)
end_time = time.time()
elapsed_time = end_time - start_time
sales_result_export(final_sales_quanity)

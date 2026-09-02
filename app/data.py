import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OLIST_DIR = os.path.join(BASE_DIR, "data", "olist")
BITEXT_DIR = os.path.join(BASE_DIR, "data", "bitext")

CUSTOMER_PATH = os.path.join(OLIST_DIR, "olist_customers_dataset.csv")
ORDER_PATH = os.path.join(OLIST_DIR, "olist_orders_dataset.csv")
ORDER_ITEM_PATH = os.path.join(OLIST_DIR, "olist_order_items_dataset.csv")
PRODUCT_PATH = os.path.join(OLIST_DIR, "olist_products_dataset.csv")
CATEGORY_TRANSLATION_PATH = os.path.join(OLIST_DIR, "product_category_name_translation.csv")
SUPPORT_PATH = os.path.join(BITEXT_DIR, "Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")

customers = pd.read_csv(CUSTOMER_PATH)
orders = pd.read_csv(ORDER_PATH)
order_items = pd.read_csv(ORDER_ITEM_PATH)
products = pd.read_csv(PRODUCT_PATH)
category_translation = pd.read_csv(CATEGORY_TRANSLATION_PATH)
support = pd.read_csv(SUPPORT_PATH)

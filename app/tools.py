from langchain.tools import tool

from app.data import (
    get_customer_orders,
    get_order_details,
    get_product_details,
)


@tool
def customer_orders(customer_unique_id: str):
    """Get all orders belonging to a customer."""
    orders = get_customer_orders(customer_unique_id)

    return orders.to_dict(orient="records")


@tool
def order_details(order_id: str):
    """Get details and items of an order."""
    order, items = get_order_details(order_id)

    return {
        "order": order.to_dict(orient="records"),
        "items": items.to_dict(orient="records"),
    }


@tool
def product_details(product_id: str):
    """Get product details including its English category."""
    product = get_product_details(product_id)

    return product.to_dict(orient="records")

from models import Customer, MenuItem, Menu, Order


def test_calculate_total_with_multiple_items():
    # A $10 burger and a $5 soda should total $15
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 10.00, "Entrees", 4.8))
    order.add_item(MenuItem("Large Soda", 5.00, "Drinks", 4.2))
    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    # An order with no items should return $0
    order = Order()
    assert order.calculate_total() == 0.0


def test_filter_by_category_returns_only_matching():
    # Filtering "Drinks" should return only drink items
    menu = Menu()
    menu.add_item(MenuItem("Large Soda", 2.49, "Drinks", 4.2))
    menu.add_item(MenuItem("Spicy Burger", 10.99, "Entrees", 4.8))
    menu.add_item(MenuItem("Lemonade", 3.00, "Drinks", 4.5))

    drinks = menu.filter_by_category("Drinks")
    assert len(drinks) == 2
    assert all(item.category == "Drinks" for item in drinks)


def test_sort_by_popularity_descending():
    # Items should be returned highest rating first
    menu = Menu()
    menu.add_item(MenuItem("Cheese Fries", 3.99, "Sides", 3.5))
    menu.add_item(MenuItem("Chocolate Brownie", 4.50, "Desserts", 4.7))
    menu.add_item(MenuItem("Spicy Burger", 10.99, "Entrees", 4.8))

    sorted_items = menu.sort_by_popularity()
    ratings = [item.popularity_rating for item in sorted_items]
    assert ratings == sorted(ratings, reverse=True)


def test_customer_purchase_history_records_order():
    # Adding an order to history should increase history length by 1
    customer = Customer("Alex")
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 10.99, "Entrees", 4.8))
    customer.add_to_history(order)
    assert len(customer.purchase_history) == 1
    assert customer.purchase_history[0] is order

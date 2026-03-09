# ByteBites — Core Models
#
# Four classes that make up the ByteBites backend:
#   Customer  - a registered user with a name and purchase history
#   MenuItem  - a food/drink item with name, price, category, and popularity rating
#   Menu      - the full catalog of items, with filtering and sorting
#   Order     - a single transaction grouping items and computing the total


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_to_history(self, order):
        self.purchase_history.append(order)


class MenuItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)


if __name__ == "__main__":
    # Manual check — create sample objects and inspect them

    burger = MenuItem("Spicy Burger", 10.99, "Entrees", 4.8)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 4.2)
    fries = MenuItem("Cheese Fries", 3.99, "Sides", 4.5)
    brownie = MenuItem("Chocolate Brownie", 4.50, "Desserts", 4.7)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)
    menu.add_item(brownie)

    print("All items:")
    for item in menu.items:
        print(f"  {item.name} - ${item.price} [{item.category}] rating: {item.popularity_rating}")

    print("\nDrinks:")
    for item in menu.filter_by_category("Drinks"):
        print(f"  {item.name}")

    print("\nSorted by popularity:")
    for item in menu.sort_by_popularity():
        print(f"  {item.name} ({item.popularity_rating})")

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print(f"\nOrder total: ${order.calculate_total():.2f}")

    customer = Customer("Alex")
    customer.add_to_history(order)
    print(f"\n{customer.name}'s purchase history: {len(customer.purchase_history)} order(s)")

# Client Feature Request

We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.

These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.

We also need a way to manage the full collection of items: a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".

Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost.

## Candidate Classes

1. **Customer** — Represents a registered user. Stores the customer's name and a list of past orders (purchase history).
2. **MenuItem** — Represents a single food or drink item on the menu. Stores name, price, category, and popularity rating.
3. **Menu** — Represents the full catalog of available items. Holds a list of MenuItem objects and supports filtering by category.
4. **Order** — Represents a single transaction. Groups selected MenuItem objects together and computes the total cost.
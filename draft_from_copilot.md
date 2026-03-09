# Draft UML Diagram (from Copilot)

This is the initial draft generated using Copilot Chat (Ask Mode) with `bytebites_spec.md` attached as context.

---

## Initial AI Output

```
+------------------+          +---------------------+
|    Customer      |          |      MenuItem        |
+------------------+          +---------------------+
| - name: str      |          | - name: str          |
| - email: str     |          | - price: float       |
| - password: str  |          | - category: str      |
| - purchase_history: list|   | - popularity: float  |
| - loyalty_points: int|      | - description: str   |
| - is_verified: bool|        | - image_url: str     |
+------------------+          +---------------------+
| + verify_user()  |          | + apply_discount()  |
| + get_history()  |          | + get_formatted_price()|
| + add_points()   |          +---------------------+
+------------------+

+------------------+          +---------------------+
|      Menu        |          |       Order         |
+------------------+          +---------------------+
| - items: list    |          | - customer: Customer|
| - last_updated   |          | - items: list        |
| - is_active: bool|          | - order_id: str      |
+------------------+          | - timestamp: str     |
| + filter_by_category()|     | - status: str        |
| + add_item()     |          +---------------------+
| + remove_item()  |          | + calculate_total() |
| + search_items() |          | + apply_tax()        |
| + sort_by_price()|          | + place_order()      |
+------------------+          | + cancel_order()     |
                               +---------------------+
```

---

## Review Notes

**Issues identified with this draft:**

- `Customer` has `email`, `password`, `loyalty_points`, and `is_verified` — none of these appear in the spec. The spec only mentions `name` and `purchase_history`.
- `MenuItem` has `description` and `image_url` — not in the spec. The spec lists only name, price, category, and popularity rating.
- `Menu` has `last_updated` and `is_active` — not requested.
- `Order` has `order_id`, `timestamp`, `status`, `customer` reference, `apply_tax()`, `place_order()`, and `cancel_order()` — all extra complexity beyond the spec.
- Several utility methods (`apply_discount`, `get_formatted_price`, `search_items`, etc.) are not part of the spec.

**Conclusion:** The AI over-engineered the design by adding attributes and methods that feel "realistic" but were not requested. The next step is to trim this down to exactly what the spec describes.

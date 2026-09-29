m_items = {
    "ESP-01": {"cd": "ESP-01", "n": "Espresso", "cat": "Coffee", "pr": 120.0, "is_bev": True},
    "CAP-02": {"cd": "CAP-02", "n": "Cappuccino", "cat": "Coffee", "pr": 160.0, "is_bev": True},
    "LAT-03": {"cd": "LAT-03", "n": "Vanilla Latte", "cat": "Coffee", "pr": 180.0, "is_bev": True},
    "CLD-04": {"cd": "CLD-04", "n": "Cold Brew", "cat": "Coffee", "pr": 200.0, "is_bev": True},
    "CRS-05": {"cd": "CRS-05", "n": "Croissant", "cat": "Bakery", "pr": 120.0, "is_bev": False},
    "MUF-06": {"cd": "MUF-06", "n": "Muffin", "cat": "Bakery", "pr": 140.0, "is_bev": False}
}

def get_menu():
    return list(m_items.values())

def get_item(cd):
    c = str(cd).strip().upper()
    if c in m_items:
        return m_items[c]
    return None

def do_show_menu():
    itms = get_menu()
    print("\nCode    Name                 Category    Price")
    print("--------------------------------------------------")
    for i in itms:
        print(i["cd"].ljust(8) + i["n"].ljust(21) + i["cat"].ljust(12) + str(i["pr"]))
    print("\nModifiers: Large Size (+Rs. 40)")
    print("Add-ons  : EXTRA_SHOT (+30), OAT_MILK (+25), CARAMEL (+20), WHIPPED_CREAM (+15)")

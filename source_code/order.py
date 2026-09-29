from menu import get_item
from customizer import calc_item_pr
from billing import do_process_bill

cnt = 101

def do_order():
    global cnt
    t_str = input("Enter Table Number (1-20): ").strip()
    if not t_str.isdigit():
        print("Error: Table number must be a number.")
        return
    t = int(t_str)
    if t < 1 or t > 20:
        print("Error: Table number must be between 1 and 20.")
        return
    
    oid = "ORD-" + str(cnt)
    cnt = cnt + 1
    itms = []
    print("\nStarting order " + oid + " (Table " + str(t) + ")")

    while True:
        cd = input("\nEnter Item Code (e.g. LAT-03): ").strip().upper()
        i = get_item(cd)
        if i is None:
            print("Error: Item code not found.")
        else:
            q_str = input("Enter Quantity: ").strip()
            if not q_str.isdigit():
                print("Error: Quantity must be a number.")
            else:
                q = int(q_str)
                if q <= 0:
                    print("Error: Quantity must be at least 1.")
                else:
                    sz = "REGULAR"
                    ads = []
                    if i["is_bev"]:
                        s_in = input("Size (R for Regular, L for Large): ").strip().upper()
                        if s_in.startswith("L"):
                            sz = "LARGE"
                        print("Add-ons (1: Extra Shot, 2: Oat Milk, 3: Caramel, 4: Whipped Cream):")
                        a_in = input("Enter numbers separated by spaces, or press Enter to skip: ").strip()
                        if len(a_in) > 0:
                            for num in a_in.split():
                                if num == "1":
                                    ads.append("EXTRA_SHOT")
                                elif num == "2":
                                    ads.append("OAT_MILK")
                                elif num == "3":
                                    ads.append("CARAMEL")
                                elif num == "4":
                                    ads.append("WHIPPED_CREAM")

                    u_pr = calc_item_pr(i, sz, ads)
                    t_pr = round(u_pr * q, 2)
                    o_itm = {
                        "cd": i["cd"],
                        "n": i["n"],
                        "sz": sz if i["is_bev"] else "STANDARD",
                        "ad": ads,
                        "q": q,
                        "u_pr": u_pr,
                        "t_pr": t_pr
                    }
                    itms.append(o_itm)
                    print("Added " + str(q) + "x " + i["n"] + " (Rs. " + str(t_pr) + ")")

        m = input("\nDo you want to add another item? (y/n): ").strip().lower()
        if m != "y" and m != "yes":
            break

    if len(itms) == 0:
        print("No items ordered. Order cancelled.")
        return

    do_process_bill(oid, t, itms)
last_b = None

def calc_bill(itms):
    sub = 0.0
    for i in itms:
        sub = sub + i["t_pr"]
    sub = round(sub, 2)
    sc = round(sub * 0.05, 2)
    tax = round((sub + sc) * 0.05, 2)
    gtot = round(sub + sc + tax, 2)
    return {
        "sub": sub,
        "sc": sc,
        "tax": tax,
        "gtot": gtot
    }

def print_receipt(oid, t, itms, b):
    l = []
    l.append("==================================================")
    l.append("             BEAN & BREW ARTISAN CAFE             ")
    l.append("                    GUEST CHECK                   ")
    l.append("==================================================")
    l.append("Order ID : " + str(oid) + " (Table " + str(t) + ")")
    l.append("--------------------------------------------------")
    l.append("Item Description         Qty   Unit       Total")
    l.append("--------------------------------------------------")
    for i in itms:
        d = i["n"]
        if i["sz"] != "STANDARD":
            d = d + " (" + i["sz"][0] + ")"
        l.append(d.ljust(25) + str(i["q"]).ljust(6) + str(i["u_pr"]).ljust(11) + str(i["t_pr"]))
        if len(i["ad"]) > 0:
            l.append("  + " + ", ".join(i["ad"]))
    l.append("--------------------------------------------------")
    l.append("Subtotal       : Rs. " + str(b["sub"]))
    l.append("Service Charge : Rs. " + str(b["sc"]))
    l.append("Tax (GST 5%)   : Rs. " + str(b["tax"]))
    l.append("==================================================")
    l.append("TOTAL PAYABLE  : Rs. " + str(b["gtot"]))
    l.append("==================================================")
    l.append("             Thank you for visiting!              ")
    l.append("==================================================")
    print("\n" + "\n".join(l))

def do_process_bill(oid, t, itms):
    global last_b
    b = calc_bill(itms)
    print_receipt(oid, t, itms, b)
    last_b = (oid, t, itms, b)

def do_view_last_bill():
    if last_b is None:
        print("\nNo bill generated yet.")
        return
    oid, t, itms, b = last_b
    print_receipt(oid, t, itms, b)

def calc_item_pr(i, sz, ads):
    pr = float(i["pr"])
    if i["is_bev"]:
        sz = str(sz).strip().upper()
        if sz == "LARGE":
            pr = pr + 40.0
        elif sz == "REGULAR":
            pr = pr + 0.0
        for a in ads:
            a = str(a).strip().upper()
            if a == "EXTRA_SHOT":
                pr = pr + 30.0
            elif a == "OAT_MILK":
                pr = pr + 25.0
            elif a == "CARAMEL":
                pr = pr + 20.0
            elif a == "WHIPPED_CREAM":
                pr = pr + 15.0
    return round(pr, 2)

# todo naamgeving functie
def calculate_tip(amount):
    tax = amount * 0.21
    tip = amount * 0.15
    total = amount + tip + tax

    print("Tax: " + format(tax, ".3f") + ",")
    print("Tip: " + format(tip, ".3f") + ",")
    print("Total: " + format(total, ".3f"))

calculate_tip(23.60)
calculate_tip(155.24)
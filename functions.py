def currency_converter(amount, currency):
    if currency == "GBP to USD":
        rate = 1.26
    elif currency == "GBP to JPY":
        rate = 191.19
    elif currency == "GBP to EUR":
        rate = 1.17

    new_amount = round(amount * rate, 2)
    return new_amount


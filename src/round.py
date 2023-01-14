def round_cash_json(lst, key):
    for x in lst:
        x[key] = round(x[key], 2)
    return lst
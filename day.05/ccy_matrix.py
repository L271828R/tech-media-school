from currency import Currency
from itertools import combinations

def get_value(ccy_pair, arr):
    for item in arr:
        if item.name == ccy_pair:
            return item.xrate
        if item.inverse_name == ccy_pair:
            return item.inverse_xrate 


def get_lookup_matrix(curreny_list):
    rows = []
    for item in currency_list:
        row = []
        for item2 in currency_list:
            row.append(item + "/" + item2)
        rows.append(row)
    return rows

def get_populated_grid(arr, currency_list, rows):
    columns = []
    for name in currency_list:
        temp_str = "{:<12}".format(name)
        columns.append(temp_str)

    column_to_print = "".join(columns)
    print("     ", column_to_print)
    rows_with_data = []
    for row in rows:
        row_with_data = []
        for item in row:
            ans = get_value(item, arr)
            temp_str = "{:<12}".format(round(ans,4))
            row_with_data.append(temp_str)
        rows_with_data.append(row_with_data)
    return rows_with_data

def report(currency_list, arr):

    rows = get_lookup_matrix(currency_list)
    rows_with_data = get_populated_grid(arr, currency_list, rows)

    for i, name in enumerate(currency_list):
        print("")
        values = "".join(rows_with_data[i])
        print("   {} {}".format(name, values))
    print("")


def is_name_in_list(name, arr):
    found = False
    for item in arr:
        if name == item.name:
            found = True
    return found

def add_to_list(ccy, arr):
    if is_name_in_list(ccy.name, arr):
        for i, item in enumerate(arr):
            if item.name == ccy.name and item.xrate is None and ccy.xrate is not None:
                item.xrate = ccy.xrate
                item.inverse_xrate = 1/ccy.xrate
                break
    else:
        arr.append(ccy)
    return arr
                


def seed_currencies(currencies, initial_values):
    for initial_value in initial_values:
        for ccy in currencies:
            if initial_value['name'] == ccy.name:
                ccy.xrate = float(initial_value['xrate'])
                ccy.inverse_xrate = 1/float(initial_value['xrate'])

    has_values = []
    for ccy in currencies:
        if ccy.xrate is not None:
            has_values.append(ccy)
            has_values.append(Currency((ccy.den, ccy.nom), 1/ccy.xrate))

    for item in has_values:
        for item2 in has_values:
            ccy = item * item2
            if ccy is not None:
                currencies = add_to_list(ccy, currencies)

    return currencies

def ask_for_initial_values(currencies_to_ask):
    initial_values = []
    for ccy in currencies_to_ask:
        xrate = input("enter excchange rate for " + ccy)
        initial_values.append({'name': ccy,
         'xrate': xrate})
    return initial_values
    

if __name__ == '__main__':
    currencies_to_ask = ['USD/GBP', 'USD/CAD', 'USD/EUR', 'USD/AUD']
    currency_list = ['USD', 'GBP', 'CAD', 'EUR', 'AUD']
    currency_pairs = [Currency(pair, None) for pair in list(combinations( currency_list, 2))]
    initial_values = ask_for_initial_values(currencies_to_ask)
    currency_pairs = seed_currencies(currency_pairs, initial_values)
    report(currency_list,  currency_pairs)

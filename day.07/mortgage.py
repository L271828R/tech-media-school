



def payment(mortgage, interest, years):
    mort = mortgage
    n = years * 12
    r  = interest / 12
    num = r * ((1 + r) ** n)
    div = (((1 + r) ** n) - 1)
    mult = num / div
    return round(mort * mult, 4)



def get_amort_table(mortgage, interest, years):
    pmt       = (payment(mortgage, interest, years))
    arr = []
    r = interest / 12
    for i in range(1, years * 12 + 1):
        if i == 1:
            balance = mortgage

        arr.append( {'bal':balance, 'r': r, 'pmt':pmt, 'principal': pmt-(r*balance), 'new balance':balance - ( pmt - (r*balance))} )
        balance = balance - ( pmt - (r*balance) )
    return arr

if __name__ == '__main__':
    mortgage  = float(input('enter principal '))
    interest  = float(input('yearly rate '))
    years     = int(input('enter years of mortgage '))
    arr = get_amort_table(mortgage, interest, years) 
    s = "{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format("month", "balance", "rate", "pmt", "principal", "new balance")
    print(s)
    print('-'*60)
    for i, r in enumerate(arr):
        s = "{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}".format(i, round(r['bal']), r['r'], round(r['pmt']), round(r['principal']), round(r['new balance']))
        print(s)

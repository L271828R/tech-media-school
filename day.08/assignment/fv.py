




if __name__ == '__main__':
    pv = float(input('enter the future value '))
    r  = float(input('enter the rate '))
    n  = float(input('enter the number of years '))

    print( round(((1 +r) ** n) *  pv, 2)) 


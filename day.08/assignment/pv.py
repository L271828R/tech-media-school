




if __name__ == '__main__':
    fv = float(input('enter the future value '))
    r  = float(input('enter the rate '))
    n  = float(input('enter the number of years '))

    print( round(fv / ((1 +r) ** n) , 2))


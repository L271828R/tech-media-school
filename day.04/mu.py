



import matplotlib.pyplot as plt



if __name__ == '__main__':
    print('Welcome to MU grapher')
    product = input("please enter a product. ")
    max_quantity = int(input("please enter the max quantity. "))

    y = []
    x = []
    for i in range(1, max_quantity + 1):
        mu = input("What is your added happiness for an extra " + product + "? ")
        x.append(i)
        y.append(int(mu))

    plt.plot(x, y, '-ro')
    plt.ylabel("Marginal Utility")
    plt.xlabel(product)
    plt.show()




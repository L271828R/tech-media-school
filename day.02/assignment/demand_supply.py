import csv
import matplotlib.pyplot as plt



if __name__ == '__main__':
    print('hello demand supply')
    supply_arr = []
    demand_arr = []
    prices_arr = []
    arr = []
    with open('data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for count, row in enumerate(reader):
            if count != 0:
                arr.append(row)
                prices_arr.append(float(row[0]))
                supply_arr.append(float(row[1]))
                demand_arr.append(float(row[2]))
    
    plt.plot(prices_arr, supply_arr)
    plt.plot(prices_arr, demand_arr)
    print('prices_arr=' , prices_arr)
    print('supply_arr=' , supply_arr)
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.axis([min(prices_arr), max(prices_arr), min(supply_arr), max(supply_arr)])
    for item in arr:
        print(item)
    plt.show()

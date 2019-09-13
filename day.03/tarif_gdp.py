


import csv
import numpy as np
import matplotlib.pyplot as plt
import random

def get_csv_contents(name, skip_row=0):
    arr = []
    with open(name) as f:
        reader = csv.reader(f)
        for count, row in enumerate(reader):
            if count > skip_row:
                arr.append(row)
    return arr
        

if __name__ == '__main__':
    print('hello tariff gdp')
    tarif_data = get_csv_contents('world_bank_tarif.csv', 5)
    gdp_data = get_csv_contents('world_bank_gdp.csv')
    
    combination = []
    for tarif in tarif_data:
        for gdp in gdp_data:
            if tarif[1] in gdp[1]:
                if tarif[2] != "" and gdp[2] != "":
                    combination.append({'name': tarif[0],
                        'iso_code': tarif[1],
                        'tarif': tarif[2],
                        'gdp': gdp[2]
                    })

    
    random_index = []   
    for i in range(0, 10):
        num = random.randint(0,len(combination)-1)
        if num not in random_index:
            random_index.append(num)

    x = []
    y = []

    for i in random_index:
        print(combination[i]['name'], combination[i]['tarif'], combination[i]['gdp'])
        x.append(float(combination[i]['tarif']))
        y.append(float(combination[i]['gdp']))
    
    plt.scatter(x, y)
    plt.xlabel('tarif')
    plt.ylabel('gdp')
    plt.show()


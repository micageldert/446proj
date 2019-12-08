import csv
import sys
import random

def main():
    x_arr = []
    y_arr = []
    z_arr = []
    with open(sys.argv[1]) as tsvfile:
        reader = csv.reader(tsvfile, delimiter ='\t')
        for row in reader:
            x_arr.append(float(row[2]))
            y_arr.append(float(row[3]))
            z_arr.append(float(row[4]))
    print(x_arr)
    print(" ")
    randFaults(x_arr)
    #randFaults(y_arr)
    #randFaults(z_arr)
    print(x_arr)

def randFaults(arr):
    for i in range(5):
        rand_idx = random.randint(0, len(arr))
        num = random.randint(-67, 67)
        arr[rand_idx] = num
    
    


if __name__ == "__main__":
    main()

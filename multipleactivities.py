import csv
import sys

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
    print(difArray(x_arr, y_arr, z_arr))
#    print(dif_arr)
#    avg = getAvg(dif_arr)

def difArray(arr, arr2, arr3):
    dif_arr = []
    dif_arr2 = []
    dif_arr3 = []
    idle = 0
    for i in range(len(arr)-1):
        while (abs(arr[i+1] - arr[i]) < 0.5 and abs(arr2[i+1] - arr2[i]) < 0.5 and abs(arr3[i+1] - arr3[i]) < 0.5):
            idle += 1 
        while (abs(arr[i+1] - arr[i]) < 0.5 and abs(arr2[i+1] - arr2[i]) < 0.5 and abs(arr3[i+1] - arr3[i]) < 0.5):
            dif_arr.append(abs(arr[i+1] - arr[i]))
            dif_arr2.append(abs(arr2[i+1] - arr2[i]))
            dif_arr3.append(abs(arr3[i+1] - arr3[i]))
            dif_arr_total.append(dif_arr)
            dif_arr_total.append(dif_arr2)
            dif_arr_total.append(dif_arr3)
    return idle 

def getAvg(arr):
    acc = 0
    for i in range(len(arr)):
        acc += arr[i]
    if len(arr) == 0:
        print("no dif values")
        return 0
    else:
        print(acc/len(arr) - 0.5)
        return (acc/len(arr) - 0.5)

if __name__ == "__main__":
    main()

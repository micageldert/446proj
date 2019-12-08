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
    
    if (len(sys.argv) > 3):
        if (sys.argv[2] == 'f'):
            randFaults(z_arr, int(sys.argv[3]))
            randFaults(y_arr, int(sys.argv[3]))
            randFaults(x_arr, int(sys.argv[3]))

    print("raw data")
    print(z_arr)
    
    findFaults(z_arr)            
    findFaults(y_arr)            
    findFaults(x_arr)            

    print("after finding faults, before differentiation")
    print(z_arr)

    dif_arrz = difArray(z_arr) 
    dif_arry = difArray(y_arr)
    dif_arrx = difArray(x_arr)
    
    print("differential data")
    print(dif_arrz)
    
    avgx = getAvg(dif_arrx)
    avgy = getAvg(dif_arry)
    avgz = getAvg(dif_arrz)
    
    classify(avgx, avgy, avgz)


def difArray(arr):
    dif_arr = []
    for i in range(len(arr)-1):
        if (abs(arr[i+1] - arr[i]) > 0.5):
            dif_arr.append(abs(arr[i+1] - arr[i]))
    return dif_arr


def findFaults(arr):
    for i in range(len(arr) - 2):
        if (abs(arr[i+1]) - abs(arr[i]) > 10):
            arr[i+1] = arr[i]
#            arr[i+1] = (arr[i+2] + arr[i])/2
#        if (arr[i+1] - arr[i] < 5):
#            arr[i] = (arr[i+1] + arr[i-1])/2


def classify(avgx, avgy, avgz):
    avg = (avgx + avgy + avgz)/3.0
    print(avg)
    if (avg <= 0.1):
        print("idle")  
    if (avg > 0.1 and avg < 0.9):
        print("standing up")
    if (avg > 0.9):
        print("falling down")


def getAvg(arr):
    acc = 0
    for i in range(len(arr)):
        acc += arr[i]
    if len(arr) == 0:
        return 0
    else:
        return (acc/len(arr) - 0.5)


def randFaults(arr, faults):
    for i in range(faults):
        rand_idx = random.randint(0, len(arr)-1)
#        num = random.randint(-67, 67)
        num = random.randint(-27, 27)
        arr[rand_idx] = num


if __name__ == "__main__":
    main()

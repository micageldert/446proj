import csv
import sys
import random
import numpy

def main():
    x_arr = []
    y_arr = []
    z_arr = []
    time = []
    with open(sys.argv[1]) as tsvfile:
        reader = csv.reader(tsvfile, delimiter ='\t')
        for row in reader:
            time.append(float(row[1]))
            x_arr.append(float(row[2]))
            y_arr.append(float(row[3]))
            z_arr.append(float(row[4]))
    
    if (len(sys.argv) > 2):
        if (sys.argv[2] == 'f'):
            randFaults(z_arr, int(sys.argv[3]))
            randFaults(y_arr, int(sys.argv[3]))
            randFaults(x_arr, int(sys.argv[3]))
        elif (sys.argv[2] == 's'):
            stuckFaults(z_arr, y_arr, x_arr)
    
    z_arr2 = filterOutliers(z_arr)
    y_arr2 = filterOutliers(y_arr)
    x_arr2 = filterOutliers(x_arr)

    with open('./output.tsv', 'wt') as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerows(zip(time, x_arr, y_arr, z_arr))

    stuckz = findStuckFaults(z_arr2, "z")
    stucky = findStuckFaults(y_arr2, "y")
    stuckx = findStuckFaults(x_arr2, "x")
    if (stuckx or stucky or stuckz):
        return 0

    dif_arrz = difArray(z_arr2) 
    dif_arry = difArray(y_arr2)
    dif_arrx = difArray(x_arr2)
    
    avgx = getAvg(dif_arrx)
    avgy = getAvg(dif_arry)
    avgz = getAvg(dif_arrz)
    avg = (avgx + avgy + avgz)/3.0
#    print("avgx " + str(avgx) + " avgy " + str(avgy) + " avgz " + str(avgz)) 
#    print("avg " + str(avg)) 
    
    classify(avgx, avgy, avgz)


def difArray(arr):
    dif_arr = []
    for i in range(len(arr)-1):
        dif_arr.append(abs(arr[i+1] - arr[i]))
    return dif_arr

def filterOutliers(arr):
    data = numpy.array(arr)
    mean = numpy.mean(data, axis = 0)
    sd = numpy.std(data, axis = 0)
    filtered = [x for x in arr if ((x > mean - 2 * sd) and (x < mean + 2 * sd))]
    return filtered


def classify(avgx, avgy, avgz):
    avg = (avgx + avgy + avgz)/3.0
    if (avg <= 0.025):
        print("Activity: Sitting")  
    elif (avg > 0.025 and avg < 0.07):
        print("Activity: Standing Up")
    elif (avg > 0.07 and avg < 1.00):
        print("Activity: Falling Down")
    else:
        print("Activity not recognized")

def getAvg(arr):
    acc = 0
    for i in range(len(arr)):
        acc += arr[i]
    if len(arr) == 0:
        return 0
    else:
        return (acc/len(arr))

def stuckFaults(zarr, yarr, xarr):
    xyz = []
    xyz.append(zarr)  
    xyz.append(yarr)  
    xyz.append(xarr)  
    arr = random.choice(xyz)
    if (arr == zarr):
        print('Stuck-at fault injected in z-array')
    if (arr == yarr):
        print('Stuck-at fault injected in y-array')
    if (arr == xarr):
        print('Stuck-at fault injected in x-array')
    rand_idx = random.randint(0, len(arr)-(int(len(arr)/6)))
    stuckval = arr[rand_idx] 
    for i in range(rand_idx, len(arr)):
        arr[i] = stuckval

def findStuckFaults(arr, axis):
    stuck = False
    data = numpy.array(arr)
    for x in range(10):
        var = numpy.var(data[int(x/10.0 * len(arr)) : int(((x+1)/10.0*len(arr)))])
        if (var < 0.000001): 
            stuck = True
    
    if (stuck == True):
        print("Stuck-at fault identified in " + axis + "-array")
    return stuck
    

def randFaults(arr, faults):
    data = numpy.array(arr)
    mean = numpy.mean(data, axis = 0)
    sd = numpy.std(data, axis = 0)

    for i in range(faults/2):
        sd_mult = random.uniform(3.0, 4.0)
        rand_idx = random.randint(0, len(arr)-1)
        num = random.uniform(mean + sd*3, mean + sd*sd_mult)
        arr[rand_idx] = num

    for i in range(faults/2, faults):
        sd_mult = random.uniform(3.0, 4.0)
        rand_idx = random.randint(0, len(arr)-1)
        num = random.uniform(mean - sd*3, mean - sd*sd_mult)
        arr[rand_idx] = num


if __name__ == "__main__":
    main()

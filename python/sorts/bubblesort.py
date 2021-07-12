import csv
import time
start_time = time.time()

# Import and read the csv file
csvFile = "babies-first-names-top-100-boys.csv"
names = []
year = []

with open(csvFile, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row.get('FirstForename'))
        year.append(row.get('yr'))


# Bubblesort Algo
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
# Bubblesort Algo Unique


def bubblesortUnique(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)
    arr = temp
    return arr


if __name__ == '__main__':
    # Unsorted
    # print(names)

    # Mergesort
    print(bubblesort(names))

    # Mergesort Unique
    # print(bubblesortUnique(names))

    print("--- %s seconds ---" % (time.time() - start_time))

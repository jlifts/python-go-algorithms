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


# Smallest Element in Array


def findSmallest(names):
    smallest = names[0]
    smallest_index = 0
    for i in range(1, len(names)):
        if names[i] < smallest:
            smallest = names[i]
            smallest_index = i
    return smallest_index

# Selection Sort Algo


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def uniqueSelectionSort(arr):
    uniqueArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        uniqueArr.append(arr.pop(smallest))
    temp = []
    for i in uniqueArr:
        if i not in temp:
            temp.append(i)
    uniqueArr = temp
    return uniqueArr


if __name__ == '__main__':
    # Unsorted
    # print(names)

    # Selection Sort
    print(selectionSort(names))

    # Selection Sort with unique names
    # print(uniqueSelectionSort(names))

    print("--- %s seconds ---" % (time.time() - start_time))

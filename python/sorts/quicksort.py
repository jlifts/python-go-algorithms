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


# Quicksort Algo
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

# Quicksort Algo Unique


def quicksortUnique(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        uniqueArr = quicksort(less) + [pivot] + quicksort(greater)
        temp = []
        for i in uniqueArr:
            if i not in temp:
                temp.append(i)
        uniqueArr = temp
        return uniqueArr


if __name__ == '__main__':
    # Unsorted
    # print(names)

    # Quicksort
    print(quicksort(names))

    # Unique Quicksort
    # print(quicksortUnique(names))

    print("--- %s seconds ---" % (time.time() - start_time))

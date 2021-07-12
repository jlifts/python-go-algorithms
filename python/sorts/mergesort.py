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


# Mergesort Algo
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursion
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
# Mergesort Algo Unique


def mergesortUnique(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # Recursion
        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

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
    print(mergesort(names))

    # Mergesort Unique
    # print(mergesortUnique(names))

    print("--- %s seconds ---" % (time.time() - start_time))

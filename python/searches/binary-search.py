import csv
import time

# Import and read the csv file
csvFile = "../../babies-first-names-top-100-boys.csv"
names = []
year = []

with open(csvFile, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row.get('FirstForename'))
        year.append(row.get('yr'))

# variable of search name
name = "Bryan"
names.sort()
year.sort()
amount = len(names)
start_time = time.time()
# Bianary Algo


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    position = binary_search(names, name)
    print(
        f"The name: {name} is located at position: {position} out of {amount}")
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(names)

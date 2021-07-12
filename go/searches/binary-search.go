package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"sort"
)

//Struct
type Record struct {
	Name string
	//Year string
}

//Variables
var name = []Record{
	Name == "Bryan"}
var data []Record

//Load the CSV names
func ReadCSV() {
	csvFile, err := os.Open("babies-first-names-top-100-boys.csv")
	if err != nil {
		log.Fatalln("Couldn't open the csv file", err)
	}
	defer csvFile.Close()

	csvLines, err := csv.NewReader(csvFile).ReadAll()
	if err != nil {
		fmt.Println(err)
	}

	//convert the multi-dimentional array of strings into an array of struct

	for _, line := range csvLines {
		row := Record{
			// Year: line[0],
			Name: line[2],
		}
		data = append(data, row)
		sort.SliceStable(data, func(i, j int) bool {
			return data[i].Name < data[j].Name
		})
	}
}

//Binary Search of an array
func binarySearch(list []int, item int) int {
	low := 0
	high := len(list) - 1
	//ToDo find how to make all ints from string args

	for low <= high {
		var mid int = (low + high) / 2
		var guess int = list[mid]
		if guess == item {
			return mid
		} else if guess > item {
			high = mid - 1
		} else {
			low = mid + 1
		}
		return mid
	}
}

//Or by built in func
func builtInBinary() {
	i := sort.Search(len(data), func(i int) bool { return name <= data[i] })
	if i < len(data) && data[i] == name {
		fmt.Printf("Found %s at index %d in %v.\n", name, i, data)
	} else {
		fmt.Printf("Did not find %s in %v.\n", name, data)
	}
}

func main() {
	ReadCSV()
	// fmt.Println(data)

	//For Binary Search
	var position = binarySearch(data, name)
	fmt.Println("The name is located at position: ", position)

	//For Selection Sort

}

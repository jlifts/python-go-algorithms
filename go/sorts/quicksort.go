package main

import "fmt"

func quicksort(list []int) []int {
	if len(list) < 2 {
		return list
	} else {
		//Pivot at the first index
		pivot := list[0]

		var less = []int{}
		var greater = []int{}
		for _, num := range list[1:] {
			if pivot > num {
				less = append(less, num)
			} else {
				greater = append(greater, num)
			}
		}

		less = append(quicksort(less), pivot)
		greater = quicksort(greater)
		return append(less, greater...)
	}
}

func main() {
	fmt.Println(quicksort([]int{10, 5, 2, 3, 6, 8, 9, 0}))
}

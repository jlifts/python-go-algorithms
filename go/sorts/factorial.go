package main

import "fmt"

func fact(x int) int {
	if x == 0 {
		return 1
	}

	return x * fact(x-1)
}

func main() {
	var num int

	// Taking input from user
	fmt.Println("Enter A Number to get Factorial: ")
	fmt.Scanln(&num)
	fmt.Println(fact(num))
}

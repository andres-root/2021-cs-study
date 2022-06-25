package main

import (
	"fmt"
)

func two_sum_ordered(arr []int, k int) bool {
	i := 0
	j := 0

	for i < j {
		acc := arr[i] + arr[j]

		if acc == k {
			return true
		} else if acc < k {
			i++
		} else {
			j--
		}
	}
	return false
}

func two_sum(arr []int, k int) []int {
	mem := make(map[int]int)

	for i := 0; i < len(arr); i++ {
		rest := k - arr[i]

		if val, ok := mem[rest]; ok {
			result := []int{val, i}
			return result
		} else {
			mem[arr[i]] = i
		}
	}
	return []int{}
}

func main() {
	arr := []int{1, 2, 3, 9}
	k := 8
	result := two_sum_ordered(arr, k)
	if result == false {
		fmt.Println(result, "Correct!")
	} else {
		fmt.Println(result, "Wrong!")
	}

	arr = []int{2, 7, 11, 15}
	k = 9
	result2 := two_sum(arr, k)
	if result2[0] == 0 && result2[1] == 1 {
		fmt.Println(result2, "Correct!")
	} else {
		fmt.Println(result2, "Wrong!")
	}
}

package main

import (
	"errors"
	"fmt"
)

func insert(arr []int, i int, v int) ([]int, error) {
	if i < 0 {
		return nil, errors.New("Index cannot be less than 0")
	}

	if i >= len(arr) {
		return append(arr, v), nil
	}

	arr = append(arr[:i+1], arr[i:]...)
	arr[i] = v

	return arr, nil
}

func MergeArrays(arr1 []int, arr2 []int) []int {
	i := 0
	j := 0
	for (i < len(arr1)) && (j < len(arr2)) {
		if arr1[i] > arr2[j] {
			arr1, _ = insert(arr1, i, arr2[j])
			i++
			j++
		} else {
			i++
		}
	}

	if j < len(arr2) {
		arr1 = append(arr1, arr2[j:]...)
	}
	return arr1
}

func main() {
	arr1 := []int{1, 3, 5, 7, 9}
	arr2 := []int{2, 4, 6, 8, 10}
	// arr1 := []int{1, 2, 3, 4, 5}
	// arr2 := []int{6, 7, 8, 9, 10}
	result := MergeArrays(arr1, arr2)
	fmt.Println(result)
}

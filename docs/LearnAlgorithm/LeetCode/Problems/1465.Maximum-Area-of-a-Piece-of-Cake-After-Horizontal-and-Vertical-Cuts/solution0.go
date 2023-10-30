package main

import (
	"fmt"
	"math"
	"sort"
)


func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
    sort.Ints(horizontalCuts)
    sort.Ints(verticalCuts)
    hcuts := append([]int{0}, append(horizontalCuts, []int{h}...)...)
    vcuts := append([]int{0}, append(verticalCuts, []int{w}...)...)
    max_area := 0
    for i := 0; i < len(hcuts) - 1; i++ {
        for j := 0; j < len(vcuts) - 1; j++ {
            area := (hcuts[i + 1] - hcuts[i]) * (vcuts[j + 1] - vcuts[j])
            if area > max_area {
                max_area = area
            }
        }
	}
    return max_area % (int(math.Pow(10, 9)) + 7)
}

func main() {
	res := maxArea(5, 4, []int{1,2,4}, []int{1,3})
	fmt.Println(res)
	if res != 4 {
		panic(fmt.Sprintf("expecting 4, got %d", res))
	}
}
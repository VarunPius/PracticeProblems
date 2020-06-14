package main

import "fmt"

func twoSum(nums []int, target int) []int{
  m := make(map[int]int)

  for i:=0; i<len(nums);i++{
    tmp := target - nums[i]
    fmt.Println("i ", i, tmp)
    //if val, ok => we don't use val because it raises error "val declared and not used"
    if _,ok := m[tmp]; ok{
      fmt.Println("Inside")
      return []int{m[tmp], i}
    }
    m[nums[i]] = i
    fmt.Println("m ", m)
  }
  return nil
}

func main() {
  nums := []int{2,3,5,7,9}
  var target int
  target = 7
  idx := twoSum(nums, target)

  fmt.Println("Result: ", idx)
}

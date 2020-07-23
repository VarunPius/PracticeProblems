package main

import "fmt"

type ListNode struct{
  Val int
  next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode{
  if l1 == nil{
    l1 = &ListNode{}
  }
  if l2 == nil{
    l2 = &ListNode{}
  }
  result := &ListNode{}
  result.Val = l1.Val + l2.Val

  if result.Val > 9 {
    result.Val -= 10

    if l2.next == nil{
      l2.next = &ListNode{}
    }
    l2.next.Val += 1 //Not exactly correct as running 2 times for same values will give error
  }

  if l2.next != nil || l1.next != nil{
    result.next = addTwoNumbers(l1.next, l2.next)
  }

  return result
}

func addTwoNumbers2(l1 *ListNode, l2 *ListNode) *ListNode{
  resPre := &ListNode{}
  cur := resPre
  carry := 0

  for l1 != nil || l2 != nil || carry != 0{
    sum := carry

    if l1 != nil{
      sum += l1.Val
      l1 = l1.next
    }

    if l2 != nil{
      sum += l2.Val
      l2 = l2.next
    }

    carry = sum / 10

    cur.next = &ListNode{Val: sum%10}
    cur = cur.next
  }
  return resPre.next
}

func prepL1() *ListNode{
  l := &ListNode{Val: 2}
  l.next = &ListNode{Val: 3}
  l.next.next = &ListNode{Val: 5}
  return l
}

func prepL2() *ListNode{
  l := &ListNode{Val: 3}
  l.next = &ListNode{Val: 5}
  l.next.next = &ListNode{Val: 7}
  return l
}

func displayResult(result *ListNode){
  for result != nil{
    fmt.Println(result.Val)
    result = result.next
  }
}

func main(){
  l1 := prepL1()
  l2 := prepL2()

  l3 := ListNode{Val: 5}
  l3.next = &ListNode{Val: 3}
  l4 := ListNode{Val: 5}
  l4.next = &ListNode{Val: 5}

  result1 := addTwoNumbers2(l1, l2)
  result2 := addTwoNumbers(l1, l2)
  result3 := addTwoNumbers2(&l3, &l4)
  result4 := addTwoNumbers(&l3, &l4)

  fmt.Println("Case1:")
  displayResult(result1)
  fmt.Println("Case2:")
  displayResult(result2)
  fmt.Println("Case3:")
  displayResult(result3)
  fmt.Println("Case4:")
  displayResult(result4)
}

//Solution when addTwoNumbers is run before addTwoNumbers2:
//  Case1:
//    5
//    8
//    2
//    1
//  Case2:
//    5
//    8
//    2
//    2
//  Case3:
//    0
//    9
//  Case4:
//    0
//    0
//    1

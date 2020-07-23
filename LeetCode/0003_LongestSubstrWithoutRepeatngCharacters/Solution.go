package main

import "fmt"

func lengthOfLongestSubstring1(s string) int {
    runes := []rune(s)
    //fmt.Println(runes)
    // -> [98 101 121 111 110 100 72 101 108 108 111]output for beyondHello
    //a := 0
    runeMap := make(map[rune]int)
    prelength:=0
    longest:=0

    for i, rn := range runes{
        var length int
        if val, ok := runeMap[rn]; !ok||val<i-prelength{
            length = prelength + 1
        } else {
            length = i - val
        }
        if length > longest{
            longest = length
        }
        prelength = length
        runeMap[rn] = i
    }

    return longest
}

func main(){
    result := lengthOfLongestSubstring1("bbebyondHello")
    fmt.Println(result)
    result = lengthOfLongestSubstring1("beyondHello")
    fmt.Println(result)
}

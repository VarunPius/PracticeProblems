package main

import "fmt"

var start, maxLen = 0, 1

func main(){
    s := longestPalindrome("hellovarun")
    fmt.Println(s)
    s = longestPalindrome("malayalam")
    fmt.Println(s)
    s = longestPalindrome("palayalam")
    fmt.Println(s)
}

func longestPalindrome(s string) string{
    start, maxLen = 0, 1
    if len(s) <= 1 {
        return s
    }

    for i:=0; i<len(s); i++{
        palindromeHelper(s, i, i)
        palindromeHelper(s, i, i+1)
    }

    return s[start:start+maxLen]
}

func palindromeHelper(s string, b int, e int) {
    for b>=0 && e<len(s) && s[b]==s[e]{
        b--
        e++
    }
    if maxLen < (e-b-1){
        start = b + 1
        maxLen = e-b-1
    }
}



func longestPalindrome1(s string) string {
	if len(s) < 2 {
		return s
	}

	begin, maxLen := 0, 1

	for i := 0; i < len(s); {
		if len(s)-i <= maxLen/2 {
			break
		}

		b, e := i, i
		for e < len(s)-1 && s[e+1] == s[e] {
			e++
		}

		i = e + 1

		for e < len(s)-1 && b > 0 && s[e+1] == s[b-1] {
			e++
			b--
		}

		newLen := e + 1 - b
		if newLen > maxLen {
			begin = b
			maxLen = newLen
		}
	}

	return s[begin : begin+maxLen]
}

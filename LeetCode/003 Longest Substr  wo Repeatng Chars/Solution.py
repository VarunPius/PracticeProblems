class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currMax = 0
        i = 0
        chrLst = [-1]*256

        for j in range(len(s)):
            if (chrLst[ord(s[j])] >= i):
                i = chrLst[ord(s[j])] + 1

            chrLst[ord(s[j])] = j
            currMax = max(currMax, j-i+1)

        return currMax

## ord is used to covert ascii to int
## 
## Here is a sample for operations with string literals
## To convert an integer (int type) value i to its string equivalent, use the function “str(i)”:
## 
## >>> str(-497)
## '-497'
## >>> str(000)
## '0'
## The inverse operation, converting a string s back into an integer, is written as “int(s)”:
## 
## >>> 
## >>> int("-497")
## -497
## >>> int("-0")
## 0
## >>> int ( "012this ain't no number" )
## Traceback (most recent call last):
##   File "<stdin>", line 1, in ?
## ValueError: invalid literal for int(): 012this ain't no number 
## 
## The last example above shows what happens when you try to convert a string that isn't a valid number.
## To convert a string s containing a number in base B, use the form “int(s, B)”:
## 
## >>> int ( '0F', 16 )
## 15
## >>> int ( "10101", 2 )
## 21
## >>> int ( "0177776", 8 )
## 65534
## 
## To obtain the 8-bit integer code contained in a one-character string s, use the function “ord(s)”. 
## The inverse function, to convert an integer i to the character that has code i, use “chr(i)”. 
## The numeric values of each character are defined by the ASCIIcharacter set.
## >>> chr( 97 )
## 'a'
## >>> ord("a")
## 97
## >>> chr(65)
## 'A'
## >>> ord('A')
## 65
## 
class Solution:
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                      "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    #def numberToWords(self, num: int) -> str:
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num%1000 != 0:
                res = self.helper(int(num%1000)) + self.thousands[i] + " " + res
            num = int(num/1000)
        return res.strip()

    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return self.lessThan20[n] + " "
        elif n < 100:
            return self.tens[int(n/10)] + " " + self.helper(n%10)
        else:
            return self.lessThan20[int(n/100)] + " Hundred " + self.helper(n%100)

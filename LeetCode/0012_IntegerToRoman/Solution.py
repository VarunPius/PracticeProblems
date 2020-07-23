class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_map = {1:'I', 4: 'IV', 5:'V', 9:'IX',
                   10:'X', 40:'XL', 50:'L', 90:'XC',
                   100:'C', 400:'CD', 500:'D', 900:'CM',
                   1000:'M'
                }

        keyset, rslt = sorted(num_map.keys()), []

        while num > 0:
            for key in reversed(keyset):
                while num//key > 0:
                    num -= key
                    rslt += num_map[key]

        return "".join(rslt)

if __name__ == "__main__":
    n1 = 16
    n2 = 453
    n3 = 45
    sol = Solution()
    print(sol.intToRoman(n1))
    print(sol.intToRoman(n2))
    print(sol.intToRoman(n3))

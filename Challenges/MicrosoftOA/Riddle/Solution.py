import random
import string

def generateRandom():
    return random.choice(string.ascii_lowercase)

def solution(input_str):
    str_list = list(input_str)

    for i,j in enumerate(str_list):
        if j == '?':
            donts = []
            donts.append(str_list[i-1]) if i > 0 else None
            donts.append(str_list[i+1]) if i < len(input_str)-1 else None
            replacement = generateRandom()
            while replacement in donts:
                replacement = generateRandom()
            str_list[i] = replacement
    return "".join(str_list)


def main():
    inputs = ["a?bx?c?s?c?t?s?a", "", "?", "?????", "asadas"]

    for i in inputs:
        print(f'Replaced string for {i} = {solution(i)}')

if __name__ == "__main__":
    main()

"""
You're guaranteed to have a solution. 
There're 26 alphabets, and every question mark can be replaced by at least 24 alphabets (since I only care about my left and right neighbor, if any)

So, we can greedily perform alphabet placement if it's not the same as my left and right neighbors

def fill_question_marks(s: str) -> str:
    #Time  : O(N)
    #Space : O(1), where N = len(s)
    
    s = list(s)

    # PROCESS EACH CHAR
    for i in range(len(s)):
        if s[i] == '?':

            # TRY EVERY ALPHABET FROM a - z
            for j in range(26):
                char = chr(ord('a') + j)

                # CHECK LEFT AND RIGHT
                left = i == 0 or s[i - 1] != char
                right = i == len(s) - 1 or s[i + 1] != char
                if left and right:
                    s[i] = char
                    break

    return ''.join(s)


if __name__ == "__main__":
    strings = ["ab?ac?", "rd?e?wg??", "????????"]
    [print(f"{s} --> {fill_question_marks(s)}") for s in strings]

"""
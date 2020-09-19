"""
Keep a stack of all characters that made it into the final output, stk

Push every character onto the stack until len(stk) == k

Check if the character in s which comes immediately after the top of the stack is an alphabet.

If yes, pop all alphabets from the stack until the first non-alphabet is encountered.

Right-strip the final output of all whitespaces.
"""

def crop_words(s: str, k: int) -> str:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    # KEEP A STACK OF ALL THE CHARACTERS THAT MADE IT
    stk = []

    # LOOP TILL LENGTH EXCEEDED
    i = 0
    while i < len(s) and len(stk) < k:
        stk.append(s[i])
        i += 1

    # CHECK IF WE NEED TO POP THE LAST WORD
    while i < len(s) and s[i].isalpha() and stk and stk[-1].isalpha():
        stk.pop()
    return ''.join(stk).rstrip()


if __name__ == "__main__":
    print(crop_words("codility We test coders", 0) == "")
    print(crop_words("codility We test coders", 14) == "codility We")
    print(crop_words(" co de my", 5) == " co")
    print(crop_words(" co de my", 7) == " co de")
    print(crop_words("   ", 1) == "")
    print(crop_words("   ", 2) == "")
    print(crop_words("   re", 2) == "")  # 3
    print(crop_words(" c ", 3) == " c")
    print(crop_words(" c d  ", 5) == " c d")
    print(crop_words("co de my", 5) == "co de")
    print(crop_words("Word", 4) == "Word")
    print(crop_words("codility We test coders", 23) == "codility We test coders")
    print(crop_words("withOutSpaces", 7) == "")
    print(crop_words("withOutSpaces", 14) == "withOutSpaces")
    print(crop_words("", 14) == "")
    print(crop_words("Separatedby hyphens", 14) == "Separatedby")
    print(crop_words("      Codility We test coders     ", 14) == "      Codility")  # 6
    print(crop_words("      Codility We test coders     ", 10) == "")  # 6

"""
Python 3 Solution:

def crop_words(s, k):
	if not s or k <= 0: return ""
	all_words = s.split(" ")
	cropped_s = ""
	for w in all_words:
		temp_s = cropped_s+ w
		if len(temp_s) <= k:
			cropped_s = temp_s + " "
		else:
			break
	return cropped_s.rstrip()
# RTC: O(N), Space: O(N)

Another way to do is:

def crop_words(s, k):
    if len(s) <= k:
        return s.rstrip()
    # checking if k finished in the middle of the word
    truncate_word = True if k < len(s) and s[k] != ' ' else False
    s = s[0:k]
    if truncate_word:
        while len(s) > 0 and s[-1] != ' ':
            s = s[0: -1]
    return s.rstrip()
# RTC: O(N), Space: O(1)
"""
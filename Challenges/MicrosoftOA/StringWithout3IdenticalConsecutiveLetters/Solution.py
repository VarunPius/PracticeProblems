def nocons(s: str) -> str:
    news = s[0:2]
    for i in range(2, len(s)):
        if s[i] == s[i-1] and s[i] == s[i-2]:
            # Do not append if the previous chars are the same
            continue
        else:
            news += s[i]
    return news

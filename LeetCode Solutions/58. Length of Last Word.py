def lengthOfLastWord( s: str) -> int:
    new_string = s.trim()
    return len(new_string.split(' ')[-1])

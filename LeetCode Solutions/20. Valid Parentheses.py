def solution(s):
    stack = []

    for character in s:
        if character in ['(', '{', '[']:
            stack.append(character)
        else:
            if not stack:
                return False
            popped_char = stack.pop()
            if popped_char == ')':
                if character != '(':
                    return False
            if popped_char == '}':
                if character != '{':
                    return False
            if popped_char == ']':
                if character != '[':
                    return False
    if stack:
        return False
    return True
solution("([)]")
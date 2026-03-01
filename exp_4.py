def S(s):

    if s == "":
        return True

    if s[0] == 'a' and len(s) > 1 and s[-1] == 'b':
        return S(s[1:-1])

    return False


# Test the parser
print(S("aabb"))   # Output: True
print(S("ab"))     # Output: True
print(S("aab"))    # Output: False

Part 2

def shift_reduce(s):

    stack = []

    for c in s:
        stack.append(c)

        if len(stack) >= 2 and stack[-1] == 'b' and stack[-2] == 'a':
            stack.pop()
            stack.pop()
            stack.append('S')

        elif len(stack) >= 3 and stack[-1] == 'b' and stack[-2] == 'S' and stack[-3] == 'a':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('S')

    return len(stack) == 1 and stack[0] == 'S'


# Test the parser
print(shift_reduce("aabb"))  # Output: True
print(shift_reduce("ab"))    # Output: True
print(shift_reduce("aab"))   # Output: False

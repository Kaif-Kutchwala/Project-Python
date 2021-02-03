
def isValid( s: str):
    stack = []
    brackets = {'(':')', '{':'}', '[':']'}
    for character in s:
        if character in brackets:
            stack.append(brackets[character])
        elif not stack or stack.pop() != character:
            return False
    return not stack

print(isValid("([])"))
print(isValid("([)"))
print(isValid("}[]"))
print(isValid("[[]"))


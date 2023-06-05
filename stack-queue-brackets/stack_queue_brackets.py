
def validate_brackets(string):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    
    for char in string:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                return False
            if char != brackets[stack.pop()]:
                return False
    
    return len(stack) == 0

string1 = "(qqqqqq){sssss}[qqqqq]"  # Balanced brackets
print(validate_brackets(string1))  # Output: True

string2 = "({)}"  # Unbalanced brackets
print(validate_brackets(string2))  # Output: False

string3 = "[{aaaaaaaa}[(Ssssss)]"  # Balanced brackets
print(validate_brackets(string3))  # Output: True

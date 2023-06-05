# def validate_brackets(str):
#     stack = []
#     brackets = {"(": ")", "{": "}", "[": "]"}

#     for char in str:
#         if char in brackets.keys():
#             stack.append(char)
#         elif char in brackets.values():
#             if not stack:
#                 return False
#             if char != brackets[stack.pop()]:
#                 return False

#         return True


# validate_brackets("()")

def is_balanced(string):
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
print(is_balanced(string1))  # Output: True

string2 = "({)}"  # Unbalanced brackets
print(is_balanced(string2))  # Output: False

string3 = "[{aaaaaaaa}[(Ssssss)]"  # Balanced brackets
print(is_balanced(string3))  # Output: True

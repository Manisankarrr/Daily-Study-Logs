def isValid(s: str) -> bool:
    stack = []
    mapp = {
        "]": "[",
        "}": "{",
        ")": "("
    }
    for p in s:
        if p not in mapp:
            stack.append(p)
        else:
            if not stack:
                return False
            else:
                popped = stack.pop()
                if popped != mapp[p]:
                    return False
    return not stack

if __name__ == "__main__":
    user_input = input("Enter a string with brackets to check: ")
    result = isValid(user_input)
    if result:
        print("Valid parentheses!")
    else:
        print("Invalid parentheses!")
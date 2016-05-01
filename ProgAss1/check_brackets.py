# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    z = -1
    y = 0
    for i, next in enumerate(text):
        y += 1
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, y))
            z += 1
            pass

        if next == ')' or next == ']' or next == '}':
            if z == -1:
                opening_brackets_stack.append(Bracket(next, y))
                break
            x = opening_brackets_stack[z]
            if x.Match(next):
                opening_brackets_stack.pop()
            else:
                opening_brackets_stack.append(Bracket(next, y))
                z += 1
                break
            z -= 1
            pass

    if len(opening_brackets_stack) == 0:
        print("Success")
    else:
        print(opening_brackets_stack[z].position)

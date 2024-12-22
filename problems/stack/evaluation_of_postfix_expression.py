"""
Stack | Set 4 (Evaluation of Postfix Expression)
https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/.
"""


def solution(expression):
    stack = []

    for item in expression:
        if item.isdigit():
            stack.append(item)

        else:
            val_1 = stack.pop()
            val_2 = stack.pop()

            stack.append(eval(val_2 + item + val_1))

    return result


if __name__ == "__main__":
    expression = "231*+9-"
    result = solution(expression)
    assert result == -4

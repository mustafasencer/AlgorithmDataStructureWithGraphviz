def solution(dir: dict):
    result = 0

    def inner(dir):
        nonlocal result
        for _, value in dir.items():
            if isinstance(value, dict):
                inner(value)
                continue

            result += value

    inner(dir)
    return result


def solution_v2(dir: dict):
    result = 0
    for _, value in dir.items():
        if isinstance(value, dict):
            result += solution_v2(value)
            continue

        result += value

    return result


def solution_v3(dir: dict):
    result = 0
    stack = []
    current = dir

    while current or stack:
        if current:
            stack.append()


if __name__ == "__main__":
    input = {"ali": {"veli": {"cem": 10}, "mesut": 20}}
    result = solution(input)
    assert result == 30

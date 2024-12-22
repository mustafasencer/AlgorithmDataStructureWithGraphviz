from collections import OrderedDict


def solution(array: str, k: int):
    # returns a dictionary data
    lookup = OrderedDict.fromkeys(array, 0)
    # frequency of each character
    for ch in array:
        lookup[ch] += 1
    # now extract list of all keys whose value is 1
    non_repeated_dict = [key for key, value in lookup.items() if value == 1]
    # returns (k-1)th character
    if len(non_repeated_dict) < k:
        return "no output."
    return non_repeated_dict[k - 1]


if __name__ == "__main__":
    array = "tutorialspoint"
    k = 3
    result = solution(array, k)
    assert result == "a"

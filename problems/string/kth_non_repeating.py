"""
Geek for geeks
"""

from collections import OrderedDict


def kth_non_repeating(array: str, k: int):
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
    else:
        return non_repeated_dict[k - 1]


# Driver function
if __name__ == "__main__":
    array = "tutorialspoint"
    k = 3
    result = kth_non_repeating(array, k)
    assert result == "a"
    print(result)
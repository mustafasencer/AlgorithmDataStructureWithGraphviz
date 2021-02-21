from collections import OrderedDict


def kth_repeating(inp, k):
    # returns a dictionary data
    dict = OrderedDict.fromkeys(inp, 0)
    # frequency of each character
    for ch in inp:
        dict[ch] += 1
    # now extract list of all keys whose value is 1
    non_repeated_dict = [key for (key, value) in dict.items() if value == 1]
    # returns (k-1)th character
    if len(non_repeated_dict) < k:
        return 'no ouput.'
    else:
        return non_repeated_dict[k - 1]


# Driver function
if __name__ == "__main__":
    inp = "tutorialspoint"
    k = 3
    print(kth_repeating(inp, k))

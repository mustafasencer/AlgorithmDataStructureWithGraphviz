def first_non_repeating_char(chars):
    mapper = {}
    order = []
    for char in chars:
        if char in mapper:
            mapper[char] += 1
            continue
        mapper[char] = 1
        order.append(char)
    for char in order:
        if mapper[char] == 1:
            return char
    return -1


if __name__ == '__main__':
    chars = 'hkgkadahskdh'
    result = first_non_repeating_char(chars)
    print(result)

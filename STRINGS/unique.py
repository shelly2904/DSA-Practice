from collections import defaultdict


def unique(string):
    isUnique = True
    hashmap = defaultdict(int)
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                hashmap[string[i]] += 1
            else:
                hashmap[string[i]] = 1
    for k, v in hashmap.items():
        if v > 1:
            isUnique = False
            break
    return isUnique


def remove_dup(string):
    start = 0
    length = len(string)
    while start < length:
        end = length - 1
        while end > start:
            if string[start] == string[end]:
                string = string[0:end] + string[end + 1:]
                length = len(string)
            end -= 1
        start += 1
    return string


if __name__ == '__main__':
    string = 'accbbbbbbcccccaaa'
    ans = unique(string)
    print(ans)
    if not ans:
        print(remove_dup(string))

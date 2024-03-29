DICT_LENGTH = 4 ** 12 + 1


def charToInt(char: str) -> int:
    c = char[0]
    if c == 'A':
        return 1
    if c == 'C':
        return 2
    if c == 'G':
        return 3
    if c == 'T':
        return 4


def strToInt(text: str) -> int:
    result = 0
    for i in range(len(text)):
        result += charToInt(text[i]) * (4**i)
    return result


n = int(input())
dictionary = [False] * DICT_LENGTH
result = []
for _ in range(n):
    [command, keyStr] = input().split()

    key = strToInt(keyStr)
    if command == 'insert':
        dictionary[key] = True
    else:
        exist = dictionary[key]
        result.append('yes' if exist else 'no')

for s in result:
    print(s)

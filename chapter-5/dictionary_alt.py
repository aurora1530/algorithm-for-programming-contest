n = int(input())
dictionary = {}
for _ in range(n):
    [command, keyStr] = input().split()

    if command == 'insert':
        dictionary[keyStr] = True
    else:
        print('yes' if keyStr in dictionary else 'no')

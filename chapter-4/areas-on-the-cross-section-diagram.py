from typing import List


class Puddle:
    def __init__(self, left_idx: int, area: int):
        self.left_idx = left_idx
        self.area = area


grounds = input()
length = len(grounds)

stack_left: List[int] = []
stack_puddle: List[Puddle] = []

total_area = 0

for i in range(length):
    if grounds[i] == '\\':
        stack_left.append(i)
    elif len(stack_left) > 0 and grounds[i] == '/':
        left_idx = stack_left.pop()
        area = i - left_idx
        total_area += area

        new_puddle = Puddle(left_idx, area)

        while len(stack_puddle) > 0 and stack_puddle[-1].left_idx > new_puddle.left_idx:
            last_puddle = stack_puddle.pop()
            new_puddle.area += last_puddle.area
        stack_puddle.append(new_puddle)

print(total_area)

each_area = [len(stack_puddle)]
for puddle in stack_puddle:
    each_area.append(puddle.area)

print(' '.join(map(str, each_area)))

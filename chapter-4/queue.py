class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node = None


class Queue:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def enqueue(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        node.next = None

    def dequeue(self) -> Node:
        if self.head is None:
            raise RuntimeError('queueが空です。dequeueできません。')
        returnNode = self.head
        self.head = self.head.next
        return returnNode


class Process:
    def __init__(self, name: str, time: int):
        self.name = name
        self.time = time

    def run(self, time: int) -> int:
        """
        time分self.timeから引く
        return: 消費した時間を返す。
        """
        used_time = self.time if time > self.time else time
        self.time = max(self.time - time, 0)
        return used_time

    def isFinished(self) -> bool:
        return self.time == 0


[n, q] = map(int, input().split())
queue = Queue()

for _ in range(n):
    [name, time] = input().split()
    process = Process(name, int(time))
    processNode = Node(process)
    queue.enqueue(processNode)

total_time = 0
finish_count = 0
while True:
    if finish_count == n:
        break

    targetNode = queue.dequeue()
    used_time = targetNode.value.run(q)
    total_time += used_time
    if targetNode.value.isFinished():
        finish_count += 1
        print(targetNode.value.name + ' ' + str(total_time))
    else:
        queue.enqueue(targetNode)

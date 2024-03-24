class Node:
    def __init__(self, key: int):
        self.key = key
        self.prev: Node = None
        self.next: Node = None

    def isNil(self):
        return self.key is None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def insert(self, key: int):
        node = Node(key)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node

    def delete(self, key: int):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                prev = current_node.prev
                next = current_node.next
                if prev is not None:
                    prev.next = next
                if next is not None:
                    next.prev = prev
                if self.head == current_node:
                    self.head = next
                if self.tail == current_node:
                    self.tail = prev
                del current_node
                break
            current_node = current_node.next

    def deleteFirst(self):
        delete_target = self.head
        if self.tail != delete_target:
            self.head.next.prev = None
        else:
            self.tail = None
        self.head = self.head.next
        del delete_target

    def deleteLast(self):
        delete_target = self.tail
        if self.head != delete_target:
            self.tail.prev.next = None
        else:
            self.head = None
        self.tail = self.tail.prev
        del delete_target

    def printNode(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.key)
            current_node = current_node.next
        print(' '.join(map(str, result)))


n = int(input())
linkedList = LinkedList()
for _ in range(n):
    commands = input().split()
    if len(commands) == 1:
        if commands[0] == 'deleteFirst':
            linkedList.deleteFirst()
        else:
            linkedList.deleteLast()
    else:
        command = commands[0]
        key = int(commands[1])
        if command == 'delete':
            linkedList.delete(key)
        else:
            linkedList.insert(key)

linkedList.printNode()

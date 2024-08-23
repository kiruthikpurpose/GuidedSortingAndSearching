class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(f"{current.coeff}X^{current.power}")
            current = current.next
        return " + ".join(result)

ll = LinkedList()

n = int(input())
for _ in range(n):
    coeff, power = map(int, input().split())
    ll.append(coeff, power)

print(ll)

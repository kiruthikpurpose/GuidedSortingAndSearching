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

    def add(self, other):
        p1 = self.head
        p2 = other.head
        result = LinkedList()

        while p1 and p2:
            if p1.power == p2.power:
                result.append(p1.coeff + p2.coeff, p1.power)
                p1 = p1.next
                p2 = p2.next
            elif p1.power > p2.power:
                result.append(p1.coeff, p1.power)
                p1 = p1.next
            else:
                result.append(p2.coeff, p2.power)
                p2 = p2.next

        while p1:
            result.append(p1.coeff, p1.power)
            p1 = p1.next

        while p2:
            result.append(p2.coeff, p2.power)
            p2 = p2.next

        return result

# Input and Creation of Polynomials
def create_polynomial():
    ll = LinkedList()
    n = int(input())
    for _ in range(n):
        coeff, power = map(int, input().split())
        ll.append(coeff, power)
    return ll

# First Polynomial
print("Enter the first polynomial:")
p1 = create_polynomial()

# Second Polynomial
print("Enter the second polynomial:")
p2 = create_polynomial()

# Polynomial Addition
result = p1.add(p2)
print("Result of addition:")
print(result)

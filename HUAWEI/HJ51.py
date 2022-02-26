class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt


while True:
    try:
        head = Node()
        length = int(input())
        numbers = list(map(int, input().split()))
        k = int(input())
        while k:
            head.nxt = Node(numbers.pop())
            head = head.nxt
            k -= 1

        print(head.val)
    except:
        break

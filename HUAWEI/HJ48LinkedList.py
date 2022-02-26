class Node:
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#         self.length = 0
#
#     def insert(self, val1, val2):
#         cur = self.head
#         node = Node(val2)
#         while cur:
#             if cur.value == val1:
#                 node.next = cur.next
#                 cur.next = node
#                 break
#             else:
#                 cur = cur.next
#
#     def remove(self, val):
#         cur = self.head
#         pre = None
#         while cur:
#             if cur.value == val:
#                 if not pre:
#                     self.head = cur.next
#                 else:
#                     pre.next = cur.next
#             else:
#                 pre = cur
#                 cur = cur.next
#
#     def printlist(self):
#         cur = self.head
#         while cur:
#             print(cur.value, end=" ")
#             cur = cur.next
#         print()
#
#
# while True:
#     try:
#         numbers = list(map(int, input().split()))
#         L = LinkedList()
#         length = numbers[0]
#         L.length = length
#         L.head = numbers[1]
#         lists = numbers[2:-1]
#         i, j = 0, 1
#         pairs = []
#         while i < len(lists):
#             pairs.append((lists[i], lists[j]))
#             i += 2
#             j += 2
#         for p in pairs:
#             L.insert(p[1], p[0])
#         L.printlist()
#         L.remove(numbers[-1])
#         L.printlist()
#     except:
#         break


# class Node():
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class LinkedList():
    def __init__(self):
        self.head = Node()
        self.length = 0

    def insert(self, val1, val2):
        cur = self.head
        node = Node(val2)
        while cur:
            if cur.value == val1:
                node.next = cur.next
                cur.next = node
                break
            else:
                cur = cur.next

    def remove(self, val):
        cur = self.head
        pre = None
        while cur:
            if cur.value == val:
                if not pre:
                   self.head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def walk(self):
        cur = self.head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next
        print()


while True:
    try:
        nums = list(map(int, input().split()))
        L = LinkedList()
        L.length, L.head.value = nums[0], nums[1]
        lst = nums[2:-1]
        i, j, pairs = 0, 1, []
        while i < len(lst):
            pairs.append((lst[i], lst[j]))
            i += 2
            j += 2
        for p in pairs:
            L.insert(p[1], p[0])
        L.remove(nums[-1])
        L.walk()
    except:
        break


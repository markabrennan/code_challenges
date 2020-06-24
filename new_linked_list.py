class Node:
    def __init__(self, data=0, next=None):
        self.val= data
        self.next = next
    def __repr__(self):
        return f'{self.val}'

def create_test_lists():
    L1 = Node(1)
    L1.next = Node(2)
    L1.next.next = Node(4)

    L2 = Node(1)
    L2.next = Node(3)
    L2.next.next = Node(4)

    return L1, L2

class LinkedList:
    def __init__(self, data):
        if isinstance(data, list):
            d = data[0]
            self.head = Node(data)
            for i in data[1:]:
                self.add(i)

        self.head = Node(data)

    def add(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self, data):
        print(f'val to pop: {data}')

        if data == self.head.data:
            self.head = self.head.next
            return data
        cur = self.head
        while cur.next:
            print('while - cur.next.data: {cur.next.data}')
            if data == cur.next.data:
                cur.next = cur.next.next
                return data

            cur = cur.next

    def __repr__(self):
        vals = []
        cur = self.head
        vals.append(cur)
        while cur.next:
            cur = cur.next
            vals.append(cur)
        return f'{vals}'

def printl(L):
    l = []
    l.append(L.val)
    n = L.next
    while n:
        l.append(n.val)
        n = n.next
    # print(l)
    return l

def rev_sub(L, start, finish):
    dummy_head = sublist_head = Node(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    print(f'next range: {finish-start}')

    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next


def get_list_num(L):
    if L is None:
        return 0
    list_num = 0
    head = L
    mult = 1
    while head:
        list_num += head.val * mult
        mult *= 10
        head = head.next
    return list_num


def create_list_from_num(num):
    if num == 0:
        return Node(0)
    rem = num
    new_list = head = Node(None, None)
    while rem:
        rem, val = divmod(rem, 10)
        head.next = Node(val)
        head = head.next

    return new_list.next


def make_list(l):
    head = Node(l[0])
    n = head
    for i in l[1:]:
        new_node = Node(i)
        n.next = new_node
        n = n.next
    return head


def make_l1():
    L1 = Node(1)
    L1.next = Node(2)
    L1.next.next = Node(4)
    return L1


def make_l2():
    L2 = Node(1)
    L2.next = Node(3)
    L2.next.next = Node(4)
    return L2


def f(L1, L2):
    head = tail = Node()
    print(f'L1: {printl(L1)}, L2: {printl(L2)}')
    while L1 and L2:
        print(f'L1.val: {L1.val}, L2.val: {L2.val}')
        if L1.val < L2.val:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        print(f'tail list is now: {printl(head)}') 
        tail = tail.next

    print(f'after while; head is now: {printl(head)}') 
    if L1:
        print(f'L1: {printl(L1)}')
    if L2:
        print(f'L2: {printl(L2)}')
    tail.next = L1 or L2
    print(f'after last assignment; head is now: {printl(head)}') 

    return head.next


# l = LinkedList(11)
# l.add(7)
# l.add(5)
# l.add(3)
# l.add(2)


# rev_sub(l.head, 2, 4)

# # this is some text

# L1, L2, = create_test_lists()

L1 = make_l1()
L2 = make_l2()
f(L1, L2)
from collections import defaultdict


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def __str__(self):
        if self.start_node is None:
            return 'Empty list'
        # walk the list and aggregate the values into a list
        val_list = []
        n  = self.start_node
        while n is not None:
            val_list.append(str(n.item))
            n = n.ref

        return ' '.join(val_list)

    def __repr__(self):
        return self.__str__()

    def add(self, data):
        return self.insert_start(data)

    def append(self, data):
        return self.insert_end(data)

    def insert_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node


    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return

        n = self.start_node

        # Walk the list
        while n.ref is not None:
            n = n.ref

        n.ref = new_node



def main():
   pass


if __name__ == '__main__':
   main()



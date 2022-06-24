

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None

    def traverse(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = self.head
            
            return node
        
        self.tail.next = node
        self.tail = node

    def preppend(self, node):
        node.next = self.head
        self.head = node
    
    def pop(self):
        value = self.head.value
        self.head = self.head.next

        if self.head and not self.head.next:
            self.tail = None

        return value

    def remove(self, value):
        node = self.head
        prev_node = None

        while node:
            if node.value == value:
                if prev_node:
                    prev_node.next = node.next
                else:
                    self.head = node.next
                    if not node.next:
                        self.tail = None
                    return node.value

            prev_node = node
            node = node.next

        return None
                

nodeneg = Node(-1)
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node5 = Node(5)

linked_list = LinkedList()
linked_list.append(node0)
linked_list.append(node1)
linked_list.append(node2)
linked_list.append(node5)
linked_list.append(node3)
linked_list.preppend(nodeneg)

linked_list.traverse()
print('--')
linked_list.pop()
linked_list.traverse()
print('--')
linked_list.remove(5)
linked_list.traverse()
print('--')
linked_list.pop()
linked_list.traverse()
print('--')
linked_list.pop()
linked_list.traverse()
print('--')
linked_list.pop()
linked_list.traverse()
print('--')
linked_list.pop()
linked_list.traverse()

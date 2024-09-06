class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        list_iter = ''

        while itr:
            list_iter += str(itr.data) + '-->'
            itr = itr.next

        print(list_iter)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    #ll.insert_at_begin(5)
    #ll.insert_at_begin(89)
    ll.print()
    #pass

from node import Node

class TwoWayNode(Node):
    def __init__(self, data, previous = None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous


class CircleDoublelinkedlist:
    def __init__(self):
        self.head = TwoWayNode(1)
        self.tail = self.head
    
        
    def ranger(self):
        for data in range(2, 6):
            self.tail.next = TwoWayNode(data, self.tail)
            self.tail = self.tail.next
            
        

    def travel(self):
        probe = self.tail
        while probe != None:
            print(probe.data)
            probe = probe.previous


    def add_elements(self, new_final, new_start):
        self.tail = TwoWayNode(new_final, self.tail)
        self.tail.previous.next = self.tail
        new_node = TwoWayNode(new_start)
        if self.tail is None:
            self.tail = new_node
        else:
            probe = self.tail
            while probe.previous != None:
                probe = probe.previous
            probe.previous = new_node
            new_node.next = probe
            

    def circular(self):
        probe = self.tail
        while probe.previous != None:
            probe = probe.previous 
        self.tail.next = probe
        print(f'the final item "{self.tail.data}" aim: {self.tail.next.data}')

        
    def search(self, data):
        probe = self.tail

        target_item = data

        while probe != None and target_item != probe.data:
            probe = probe.previous

        if probe != None:
            print(f'target item {target_item} has been found')
        else:
            print(f'target item {target_item} is not in the linked list')
            

    def replace(self, data, new_item):
        probe = self.tail
        target_item = data

        while probe != None and target_item != probe.data:
            probe = probe.previous

        if probe != None:
            probe.data = new_item
            print(f'{new_item} replaced the old value in the node number {target_item}')
        else:
            print(f"the target item {target_item} is not in the linked list")

    def romove_element_of_tail(self):
        removed_item = self.tail.data
        
        try: 
            if self.tail.next.previous is None:
                removed_item = self.tail.data
                self.tail = self.tail.previous 
                self.tail.next = self.tail.next.next
                print(f'we remove: {removed_item}')
                print(f'Now the final item "{self.tail.data}" aim: {self.tail.next.data}')
        except AttributeError:
            probe = self.tail
            while probe.next != None:
                probe = probe.next
            removed_item = probe.data
            self.tail = self.tail.previous 
            self.tail.next = None
            print(f'we remove: {removed_item}')

    def add_item(self, new_item, index):
        try:
            index = int(index)
        except ValueError:
            print(f'El indice "{index}" no es un numero')
            return False

        if self.tail is None or index < 0:
            self.tail = TwoWayNode('py', self.tail)
        else:
            probe = self.tail.next
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1 
            if probe.next.previous is None:
                probe.next = TwoWayNode(new_item, probe, probe.next)
                self.tail = probe.next  
                print(f'the final item "{self.tail.data}" aim: {self.tail.next.data}')  
            else:
                probe.next = TwoWayNode(new_item, probe, probe.next)
                probe.next.next.previous = probe.next

    def remove_element_in_index(self, index):
        if index <= 0 or self.tail.next is None: 
            remove_item = self.tail.data
            self.tail = self.tail.next
            print(remove_item)
        else:
            probe = self.tail
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            if probe.next.next.previous is None:
                remove_item = self.tail.data
                self.tail = self.tail.previous
                self.tail.next = self.tail.next.next
                print(f'we remove: {remove_item}')
                print(f'Now the final item "{self.tail.data}" aim: {self.tail.next.data}') 
            else:   
                remove_item = probe.next.data
                probe.next = probe.next.next
                probe.next.previous = probe
                print(f'we remove: {remove_item}')

            
if __name__ == '__main__':
    words = CircleDoublelinkedlist()
    words.ranger()
    words.travel()
    words.add_elements('F', 'I')
    words.search(3)
    words.search(10)
    words.circular()
    words.replace(4, 8)
    words.romove_element_of_tail()
    words.add_item(9, 2)
    words.remove_element_in_index(5)
    
    words.travel()

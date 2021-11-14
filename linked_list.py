class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = None
for count in range(1, 6):
	head = Node(count, head)
	print (head)

number = 0
while head != None:
	head = head.next
	number  = number + 1
	print (head)
	print (number)



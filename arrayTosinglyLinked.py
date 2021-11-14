array = [2, 4, 6]
datos = SinglyLinkedList()

for i in array:
    datos.append(i)
current = datos.tail

while current:
    print(current.data)
    current = current.next
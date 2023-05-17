

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(12)  
class LinkedList:
    def __init__(self,head=None):
        self.head = head
    def append(self,new_element):
        itr = self.head
        if self.head:
            while itr.next:
                itr = itr.next
            itr.next= new_element
        else:
            self.head = new_element
            return
                
    def printLL(self):
        current = self.head
        while current is not None:
            print(str(current.value), end= " =>") 
            current = current.next
    def get_position(self,position):
        currentNode = self.head
        currentPosition = 1
        if currentNode is None:
            print('None')
        
        while currentNode:
            if currentPosition == position:
                print(currentNode.value)
                return
            currentPosition +=1
            currentNode = currentNode.next
        print('None')
    def insert_first(self, new_element):
        tempNode = self.head
        self.head = new_element
        self.head.next = tempNode
        del tempNode
        pass

    def delete_first(self):
        currentNode = self.head
        remainder = currentNode.next
        del currentNode
        self.head = remainder
        return


    def insertHead(self,new_node):
        tempNode = self.head
        self.head = new_node
        self.head.next = tempNode
        del tempNode
    def listlength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    
    def insertAt(self,position,element):
        if position < 0 or position > self.listlength():
            print('Invalid Position')
            return
        if position == 1:
            self.insertHead(element)
            return
         
        currentNode = self.head
        currentPosition = 1

        if currentNode is None:
            return None
       
        
        while currentNode:
            if currentPosition == position:
                previousNode.next = element
                element.next = currentNode
                break
            previousNode = currentNode
            currentPosition +=1
            currentNode = currentNode.next
            
    def delete(self,value):
        currentNode = self.head
        remainder = currentNode.next
        currentValue = 100
        if currentNode.value == value:
             del currentNode
             self.head = remainder
             return
        while currentNode is not None:
            if currentNode.value == value:
               previousNode.next = currentNode.next
               currentNode.next = None
               break
            previousNode = currentNode
            currentNode = currentNode.next
            
        
        
    

node4 = Node(4)
ll = LinkedList()
ll.append(node1)
ll.append(node2)
ll.append(node4)
ll.append (node3)
ll.printLL()

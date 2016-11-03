#Basic Operations of Linked List

class Node(object):
    def __init__(self, data_name):
        self.data = data_name
        self.next = None
        
        
        
class LinkedList(object):
            
    def __init__(self, head = None):
        self.head = head
                
    def insert(self, node):
        #add at the front
        node.next = self.head
        node = None
        self.head = node
        
    def insertAtEnd(self, node): 
    
        if self.head is None:
            self.head = node
            return
        
        #add at the end
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    
    def length(self, ll):
        count = 0
        cur = ll.head
        while cur.next:
            cur = cur.next
            count +=1
        return count
            
    def findMid(self, ll):
        point1 = ll.head
        point2 = ll.head
        while point1.next and (point1.next).next and ((point1.next).next).next:
            #and (((point1.next).next).next).next:
            point1 = ((point1.next).next).next
            point2 = point2.next
        return point2.data

           
if __name__=="__main__":
    l_inp = [1,2,3,9,5,6,7]
    ll = LinkedList()
    
    
    for l in l_inp:
        node = Node(l)
        ll.insertAtEnd(node)
    
    print ll.findMid(ll)

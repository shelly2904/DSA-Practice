#Reverse linked list by k nodes.

class Node(object):
    def __init__(self, data_name):
        self.data = data_name
        self.next = None
        
        
class LinkedList(object):
          
    def __init__(self, head = None):
        self.head = head
                
    def insert_at_front(self, node):
        #add at the front
        node.next = self.head
        self.head = node
        
    def insert_at_end(self, node): 
        if self.head is None:
            self.head = node
            return
        #add at the end
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
        node.next = None

    def insert_at_pos(self, node, pos):
        if not self.head and pos == 0:
            self.head = node
            return
        cur = self.head
        position = 0
        while cur:
            if position == pos:
                node.next = cur.next
                cur.next = node
                break
            else:
                position += 1
                cur = cur.next


    def traversal(self):
        current = self.head
        print ''
        print 'start of list'
        while current:
            print current.data
            current = current.next
        print 'end of list'
        print ''



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

    '''
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
            point1 = ((point1.next).next).next
            point2 = point2.next
        return point2.data


    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node=current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        ll.traversal()
        return True



    def traversal(self):
        current = self.head
        print ''
        print 'start of list'

        while current:
            print current.data
            current = current.next

        print 'end of list'
        print ''
        
        return True



    def reverse_k_nodes(self, k):
        print 'original'
        self.traversal()
        current = self.head
        count = 1
        start = self.head
        header = start
        pend = None
        while current:

            if count % k == 0 or current.next == None:
                print 'reversing list: start from', start.data, ' end: ', current.data
                print ''
                
                #keeping next pointer to start
                temp = current.next
                #prev set to None
                prev = temp
                if pend:
                    print pend.data, ' points to ', current.data
                    pend.next = current

                pend = start
                if prev:
                    print 'prev at: ', prev.data
                else:
                    print 'prev is None'
                while start != temp and start !=None:
                    next_node=start.next
                    start.next = prev
                    prev = start
                    start = next_node

                if count / k == 1:
                    self.head = current
                    print 'changed head to ', current.data

                print 'current at ', current.data               
                current = temp
                start = temp
                count +=1
               
                

                
            else:
                current = current.next
                count += 1
                #print 'current at ', current.data

        print 'reverse:'
        self.traversal()

    '''
        


           
if __name__=="__main__":
    #l_inp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    ll = LinkedList()
    #for l in l_inp:
    node = Node(1)
    ll.insert_at_end(node)
    ll.traversal()
    node = Node(4)
    ll.insert_at_front(node)
    print
    node = Node(10)
    ll.insert_at_end(node)
    ll.traversal()
    print 
    node = Node(5)
    ll.insert_at_pos(node, 2)
    ll.traversal()




    #print "Before reverse ", ll.traversal()
    #print "After reverse ", ll.reverse()

    #print "Revere every K nodes"
    #print  ll.reverse_k_nodes(4)

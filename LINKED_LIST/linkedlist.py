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


    def delete_key(self, key):
        if self.head is None:
            return "Linked List empty"
        cur = self.head
        prev = None
        while cur:
            #print cur.data, prev.data
            if cur.data == key:
                if cur == self.head:
                    self.head = self.head.next
                    cur.next = None
                else:
                    prev.next = cur.next
                    cur.next = None
                return True
            prev = cur
            cur = cur.next
        return "Key doesnot exists"


    def delete_at_pos(self, pos):
        if self.head is None:
            return "Linked List empty"
        cur = self.head
        prev = None
        position = 0
        while cur:
            #print cur.data, prev.data
            if position == pos:
                if cur == self.head:
                    self.head = self.head.next
                    cur.next = None
                else:
                    prev.next = cur.next
                    cur.next = None
                return True
            prev = cur
            cur = cur.next
            position += 1
        return "Key doesnot exists"




    def traversal(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


            
    def findMid(self, ll):
        point1 = ll.head
        point2 = ll.head
        while point1.next and (point1.next).next and ((point1.next).next).next:
            #and (((point1.next).next).next).next:
            point1 = ((point1.next).next).next
            point2 = point2.next
        return point2.data

    
    def length_iter(self):
        count = 0
        cur = self.head
        while cur.next:
            cur = cur.next
            count +=1
        return count


    def length_recur(self, cur):
        if not cur:
            return 0
        return 1+ self.length_recur(cur)


    def swap_nodes(self, X, Y):
        if self.head is None:
            return "Empty linked list"

        curX = self.head 
        prevX = None
        foundX = False
        while curX:
            if curX.data == X:
                foundX = True
                break
            else:
                prevX = curX
                curX = curX.next

        curY = self.head 
        prevY = None
        foundY = False
        while curY:
            if curY.data == Y:
                foundY = True
                break
            else:
                prevY = curY
                curY = curY.next

        if not foundY and foundX:
            return "One of the data doesnot exists"
        if prevX is None:
            temp = curX.next
            curX.next = curY.next
            prevY.next = curX
            curY.next = temp
            self.head = curY

        elif prevY is None:
            temp = curY.next
            curY.next = curX.next
            prevX.next = curY
            curX.next = temp
            self.head = curX

             
        else:
            prevX.next = curY
            prevY.next = curX
            temp = curX.next
            curX.next = curY.next
            curY.next = temp

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next_node=current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return True


    def findMid(self, ll):
        point1 = ll.head
        point2 = ll.head
        while point1.next and (point1.next).next and ((point1.next).next).next:
            point1 = ((point1.next).next).next
            point2 = point2.next
        return point2.data



    '''
            
    def findMid(self, ll):
        point1 = ll.head
        point2 = ll.head
        while point1.next and (point1.next).next and ((point1.next).next).next:
            point1 = ((point1.next).next).next
            point2 = point2.next
        return point2.data





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
    l_inp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    ll = LinkedList()
    for l in l_inp:
        node = Node(l)
        ll.insert_at_end(node)
    # ll.traversal()
    #
    # print ll.reverse()
    # ll.traversal()


    #print ll.swap_nodes(1, 14)
    #ll.traversal()
    #node = Node(4)
    #ll.insert_at_front(node)
    #print
    #node = Node(10)
    #ll.insert_at_end(node)
    #ll.traversal()
    #print 
    #node = Node(5)
    #ll.insert_at_pos(node, 2)
    #ll.traversal()

    #print 
    #print ll.delete_at_pos(5)
    #ll.traversal()

    #assert ll.length_iter() == ll.length_recur(ll.head)





    #print "Before reverse ", ll.traversal()
    #print "After reverse ", ll.reverse()

    #print "Revere every K nodes"
    #print  ll.reverse_k_nodes(4)

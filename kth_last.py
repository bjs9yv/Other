# In a singly linked list, find the kth from the last node
import time

class Node():
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
class List():
    def __init__(self):
        self.start = Node()
        self.end = self.start
    def add(self,node):
        self.end.next_node = node
        self.end = node
        
def CollinsWay(l,k):
    start = l.start
    curr = start
    length = 0
    while curr.next_node != None:
        length += 1
        curr = curr.next_node
    curr = start
    for x in range(0,length-k):
        curr = curr.next_node
    return curr.value

def Brians_way(l,k):
    curr_pointer = l.start
    delay_pointer = l.start
    delay_timer = k
    while curr_pointer.next_node != None:
        if delay_timer == 0:
            delay_pointer = delay_pointer.next_node
        else:
            delay_timer -= 1
        curr_pointer = curr_pointer.next_node
    return delay_pointer.value

if __name__ == "__main__":
    l = List()
    for x in range(0,1000000):
        l.add(Node(x))
    k = 0
    t0 = time.time()
    CollinsWay(l,k)
    t1 = time.time()
    print t1-t0
    tt0 = time.time()
    Brians_way(l,k)
    tt1 = time.time()
    print tt1-tt0
    
    

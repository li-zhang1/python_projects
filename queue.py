"""
Implement Queue
"""
class Queue:
    def __init__(self):
        self.__queueList = []
        
    def put(self,val):
        self.__queueList.insert(0,val)
    
    def get(self):
        val = self.__queueList[-1]
        del self.__queueList[-1]
        return val
        
    def result(self):
        return self.__queueList
    

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        if(Queue.result(self) == []):
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

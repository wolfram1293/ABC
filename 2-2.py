import sys

def main(lines):
    Q=int(lines[0])
    class Heap:
        def __init__(self):
            self.list=[]

        def heappush(self,a: int):
            self.list.append(a)
            index=len(self.list)-1
            while 1:
                parent=(index-1)//2
                if index==0:
                    break
                if self.list[index]>self.list[parent]:
                    self.list[index],self.list[parent]=self.list[parent],self.list[index]
                    index=parent
                else: 
                    break         

        def heappop(self):
            a=self.list[0]
            self.list[0]=self.list.pop()
            parent=0        
            while 1:
                c1=2*parent+1
                c2=2*parent+2
                if c2>len(self.list)-1:
                    c=c1
                else:
                    if self.list[c1]<self.list[c2]:
                        c=c2
                    else:
                        c=c1
                if c>=len(self.list):
                    break
                    
                if self.list[c]>self.list[parent]:
                    self.list[c],self.list[parent]=self.list[parent],self.list[c]
                    parent=c
                else:
                    break
            return a

    heap=Heap()
    for i in range(Q):
        l=[int(x.strip()) for x in lines[i+1].split()]
        if l[0]==1:
            heap.heappush(l[1])
        else:
            print(heap.heappop())
    
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
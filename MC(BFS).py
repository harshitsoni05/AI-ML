# Hello World program in Python
    
#print "Hello World!\n"

class graph :
    n = -1
    c = 1
    visited = {1 : [3,3,0,0,0]}
    node = int()
    parent = int()
    a1 = int ()
    b1 = int ()
    a2 = int ()
    b2 = int ()
    m = int () 
    # 0 for forward , 1 for backward
def twoMF(obb = graph(),p = int()) :
    print("twoMF")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a1>=2:
        obb.a1=obb.a1-2
        obb.a2=obb.a2+2
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,obb.m]
        
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(1)
            graph.n = graph.n+1
            print(graph.visited[graph.c])
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=1
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=0
        
def twoMB(obb = graph(),p = int()) :
    print("twoMB")
    #graph.n = obb.node
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a2>=2:
        obb.a1=obb.a1+2
        obb.a2=obb.a2-2
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,obb.m]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0 :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(0)
            graph.visited[graph.c]
            graph.n = graph.n+1
            print(graph.visited[graph.c])
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=0
            obj[graph.n].parent = p
            
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=1

def twoCF(obb = graph(),p = int()) :
    print("twoCF")
    #graph.n = obb.node
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.b1>=2:
        obb.b1=obb.b1-2
        obb.b2=obb.b2+2
        pp = obb.node
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,1]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(1)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoCB(obj[graph.n],pp)
            graph.n = graph.n+1
            print(graph.visited[graph.c])
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=1
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=0

def twoCB(obb = graph(),p = int()) :
    print("twoCB")
    #graph.n = obb.node
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.b2>=2:
        obb.b1=obb.b1+2
        obb.b2=obb.b2-2
        pp = obb.node
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,0]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(0)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoCF(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=0
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=1


def oneCF(obb = graph(),p = int()) :
    print("oneCF")
    #graph.n = obb.node
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.b1>=1:
        obb.b1=obb.b1-1
        obb.b2=obb.b2+1
        pp = obb.node
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,1]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(1)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneCB(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=1
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=0


def oneCB(obb = graph(),p = int()) :
    print("oneCB")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.b2>=1:
        obb.b1=obb.b1+1
        obb.b2=obb.b2-1
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,0]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0 :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(0)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneCB(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=0
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=1

def oneMF(obb = graph(),p = int()) :
    print("oneMF")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a1>=1:
        obb.a1=obb.a1-1
        obb.a2=obb.a2+1
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,1]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(1)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMB(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=1
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=0

def oneMB(obb = graph(),p = int()) :
    print("oneMB")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a2>=1:
        obb.a1=obb.a1+1
        obb.a2=obb.a2-1
        pp = obj[graph.n].node
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,0]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(0)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMF(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=0
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=1

def oneMoneCF(obb = graph(),p = int()) :
    print("oneMoneCF")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a1>=1 and obb.b1>=1:
        obb.a1=obb.a1-1
        obb.a2=obb.a2+1
        obb.b1=obb.b1-1
        obb.b2=obb.b2+1
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,1]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(1)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMoneCB(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=1
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=0
        
def oneMoneCB(obb = graph(),p = int()) :
    print("oneMoneCB")
    #graph.n = obb.node
    print(p)
    temp1=obb.a1
    temp2=obb.b1
    temp3=obb.a2
    temp4=obb.b2
    temp5=obb.m
    if obb.a2>=1 and obb.b2>=1:
        obb.a1=obb.a1+1
        obb.a2=obb.a2-1
        obb.b1=obb.b1+1
        obb.b2=obb.b2-1
        temp = []
        temp = [obb.a1 , obb.b1,obb.a2,obb.b2,0]
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obb.a1!=0 and  obb.a1<obb.b1:
            check =1
        if obb.a2!=0 and  obb.a2<obb.b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obb.a1)
            graph.visited[graph.c].append(obb.b1)
            graph.visited[graph.c].append(obb.a2)
            graph.visited[graph.c].append(obb.b2)
            graph.visited[graph.c].append(0)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMoneCF(obj[graph.n],pp)
            print(graph.visited[graph.c])
            graph.n = graph.n+1
            print(graph.n)
            obj[graph.n] = graph()
            obj[graph.n].node = graph.n
            obj[graph.n].a1=obb.a1
            obj[graph.n].b1=obb.b1
            obj[graph.n].a2=obb.a2
            obj[graph.n].b2=obb.b2
            obj[graph.n].m=0
            obj[graph.n].parent = p
    obb.a1=temp1
    obb.b1=temp2
    obb.a2=temp3
    obb.b2=temp4
    obb.m=1

obj = {}
graph.n = graph.n+1
obj[graph.n] = graph()
obj[graph.n].node=graph.n
obj[graph.n].parent=-1
obj[graph.n].a1=3
obj[graph.n].b1=3
obj[graph.n].a2=0
obj[graph.n].b2=0
obj[graph.n].m=0
a=0
while a<=graph.n:
  if obj[a].m==0:
    twoMF(obj[a],a)
    twoCF(obj[a],a)
    oneMF(obj[a],a)
    oneCF(obj[a],a)
    oneMoneCF(obj[a],a)
  else:
    twoMB(obj[a],a)
    twoCB(obj[a],a)
    oneMB(obj[a],a)
    oneCB(obj[a],a)
    oneMoneCB(obj[a],a)
  a=a+1
print(graph.visited)
final =int()
for i in range(graph.n):
    if obj[i].a1==0 and obj[i].b1==0 and obj[i].a2==3 and obj[i].b2==3:
        final = i
    
graph.n=final
print(final)
#print(obj[7].parent)
#print(obj[7].a1,obj[7].b1,obj[7].a2,obj[7].b2)
while obj[graph.n].parent != -1 :
    print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m)
    graph.n=obj[graph.n].parent
print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m)

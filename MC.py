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
    if obj[graph.n].a1>=2:
        obj[graph.n].a1=obj[graph.n].a1-2
        obj[graph.n].a2=obj[graph.n].a2+2
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        print(obj[graph.n].a1)
        print(obj[graph.n].b1)
        print(obj[graph.n].a2)
        print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            twoCB(obj[graph.n],pp)
            oneCB(obj[graph.n],pp)
            oneMB(obj[graph.n],pp)
            oneMoneCB(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2
        
        
def twoMB(obb = graph(),p = int()) :
    print("twoMB")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].a2>=2:
        obj[graph.n].a1=obj[graph.n].a1+2
        obj[graph.n].a2=obj[graph.n].a2-2
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0 :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMF(obj[graph.n],pp)
            twoCF(obj[graph.n],pp)
            oneCF(obj[graph.n],pp)
            oneMF(obj[graph.n],pp)
            oneMoneCF(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

def twoCF(obb = graph(),p = int()) :
    print("twoCF")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].b1>=2:
        obj[graph.n].b1=obj[graph.n].b1-2
        obj[graph.n].b2=obj[graph.n].b2+2
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoCB(obj[graph.n],pp)
            twoMB(obj[graph.n],pp)
            oneCB(obj[graph.n],pp)
            oneMB(obj[graph.n],pp)
            oneMoneCB(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

def twoCB(obb = graph(),p = int()) :
    print("twoCB")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].b2>=2:
        obj[graph.n].b1=obj[graph.n].b1+2
        obj[graph.n].b2=obj[graph.n].b2-2
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoCF(obj[graph.n],pp)
            twoMF(obj[graph.n],pp)
            oneCF(obj[graph.n],pp)
            oneMF(obj[graph.n],pp)
            oneMoneCF(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2


def oneCF(obb = graph(),p = int()) :
    print("oneCF")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].b1>=1:
        obj[graph.n].b1=obj[graph.n].b1-1
        obj[graph.n].b2=obj[graph.n].b2+1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneCB(obj[graph.n],pp)
            twoCB(obj[graph.n],pp)
            twoMB(obj[graph.n],pp)
            oneMB(obj[graph.n],pp)
            oneMoneCB(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2


def oneCB(obb = graph(),p = int()) :
    print("oneCB")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].b2>=1:
        obj[graph.n].b1=obj[graph.n].b1+1
        obj[graph.n].b2=obj[graph.n].b2-1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0 :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneCB(obj[graph.n],pp)
            twoCF(obj[graph.n],pp)
            twoMF(obj[graph.n],pp)
            oneMF(obj[graph.n],pp)
            oneMoneCF(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

def oneMF(obb = graph(),p = int()) :
    print("oneMF")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].a1>=1:
        obj[graph.n].a1=obj[graph.n].a1-1
        obj[graph.n].a2=obj[graph.n].a2+1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMB(obj[graph.n],pp)
            twoCB(obj[graph.n],pp)
            twoMB(obj[graph.n],pp)
            oneCB(obj[graph.n],pp)
            oneMoneCB(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

def oneMB(obb = graph(),p = int()) :
    print("oneMB")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].a2>=1:
        obj[graph.n].a1=obj[graph.n].a1+1
        obj[graph.n].a2=obj[graph.n].a2-1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMF(obj[graph.n],pp)
            twoCF(obj[graph.n],pp)
            twoMF(obj[graph.n],pp)
            oneCF(obj[graph.n],pp)
            oneMoneCF(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

def oneMoneCF(obb = graph(),p = int()) :
    print("oneMoneCF")
    #graph.n = obb.node
    print(p)
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
    print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2)
    if obj[graph.n].a1>=1 and obj[graph.n].b1>=1:
        obj[graph.n].a1=obj[graph.n].a1-1
        obj[graph.n].a2=obj[graph.n].a2+1
        obj[graph.n].b1=obj[graph.n].b1-1
        obj[graph.n].b2=obj[graph.n].b2+1
        #print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2)
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMoneCB(obj[graph.n],pp)
            twoCB(obj[graph.n],pp)
            twoMB(obj[graph.n],pp)
            oneMB(obj[graph.n],pp)
            oneCB(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2
        
def oneMoneCB(obb = graph(),p = int()) :
    print("oneMoneCB")
    #graph.n = obb.node
    print(p)
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
    if obj[graph.n].a2>=1 and obj[graph.n].b2>=1:
        obj[graph.n].a1=obj[graph.n].a1+1
        obj[graph.n].a2=obj[graph.n].a2-1
        obj[graph.n].b1=obj[graph.n].b1+1
        obj[graph.n].b2=obj[graph.n].b2-1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a1 , obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m]
        print(temp)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a1!=0 and  obj[graph.n].a1<obj[graph.n].b1:
            check =1
        if obj[graph.n].a2!=0 and  obj[graph.n].a2<obj[graph.n].b2:
            check =1
        if check == 0:
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a1)
            graph.visited[graph.c].append(obj[graph.n].b1)
            graph.visited[graph.c].append(obj[graph.n].a2)
            graph.visited[graph.c].append(obj[graph.n].b2)
            graph.visited[graph.c].append(obj[graph.n].m)
            #print("updated ")
            #print(graph.visited)
            
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #oneMoneCF(obj[graph.n],pp)
            twoCF(obj[graph.n],pp)
            twoMF(obj[graph.n],pp)
            oneMF(obj[graph.n],pp)
            oneCF(obj[graph.n],pp)
    obj[graph.n].a1=obb.a1
    obj[graph.n].b1=obb.b1
    obj[graph.n].a2=obb.a2
    obj[graph.n].b2=obb.b2

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
twoMF(obj[graph.n])
twoCF(obj[graph.n])
#twoCB(obj[graph.n],1)
oneCF(obj[graph.n])
#oneCB(obj[graph.n],1)
oneMF(obj[graph.n])
#oneMB(obj[graph.n],1)
oneMoneCF(obj[graph.n])
#oneMoneCB(obj[graph.n],1)
print(graph.visited)
final =int()
for i in range(graph.n):
    if obj[i].a1==0 and obj[i].b1==0 and obj[i].a2==3 and obj[i].b2==3:
        final = i
        break
graph.n=final
print(final)
#print(obj[7].parent)
#print(obj[7].a1,obj[7].b1,obj[7].a2,obj[7].b2)
while obj[graph.n].parent != -1 :
    print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m)
    graph.n=obj[graph.n].parent
print(obj[graph.n].a1,obj[graph.n].b1,obj[graph.n].a2,obj[graph.n].b2,obj[graph.n].m)
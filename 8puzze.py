# Hello World program in Python
    
#print "Hello World!\n"
goal =[1,2,3,4,5,6,7,8,0]
class graph :
    target=int()
    stop=0
    n = -1
    c = 1
    #visited = {1 : [3,2,6,0,8,4,7,5,1]}
    node = int()
    parent = int()
    a = {}
    a[1] = int ()
    a[2] = int ()
    a[3] = int ()
    a[4] = int ()
    a[5] = int ()
    a[6] = int ()
    a[7] = int ()
    a[8] = int ()
    a[9] = int () 
    b = int()
    lock = []
def up(obb = graph(),p = int()) :
    #print("up")
    #test=0
    #graph.n = obb.node
    #print(p)
    #print(graph.visited)
    '''graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=obj[p].a[1]
    obj[graph.n].a[2]=obj[p].a[2]
    obj[graph.n].a[3]=obj[p].a[3]
    obj[graph.n].a[4]=obj[p].a[4]
    obj[graph.n].a[5]=obj[p].a[5]
    obj[graph.n].a[6]=obj[p].a[6]
    obj[graph.n].a[7]=obj[p].a[7]
    obj[graph.n].a[8]=obj[p].a[8]
    obj[graph.n].a[9]=obj[p].a[9]
    obj[graph.n].b=obj[p].b
    print(obj[graph.n].b)
    obj[graph.n].parent = p'''
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            y=y+3
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[2]!=0 and obj[graph.n].a[3]!=0 and check==0:
        #print(obj[graph.n].b)
        #obj[graph.n].b=obj[graph.n]-3
        #print(obj[graph.n].a[7])
        print("up")
        temp=obj[graph.n].b
        temp=temp-3
        #print(obj[graph.n].a[obj[graph.n].b])
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
        #test=1
        #print(obj[graph.n].a[obj[graph.n].b])
        #print(obj[graph.n].a[7])
        #pp = obj[graph.n].node
        #temp = []
        #temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        #print(temp)
        #print(obj[graph.n].b)
        #check = 0
        '''for i in graph.visited:
            if graph.visited[i] == temp :
                check = 1
        if obj[graph.n].a[1]==1 and obj[graph.n].a[2]==3 and obj[graph.n].a[5]==2 :
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.c
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                right(obj[pp],pp)
            if graph.stop==0:
                left(obj[pp],pp)
            if graph.stop==0:
                up(obj[pp],pp)'''
    '''if test==1:
        temp=obj[graph.n].b
        temp=temp+3
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
    obj[graph.n].a[1]=obb.a[1]
    obj[graph.n].a[2]=obb.a[2]
    obj[graph.n].a[3]=obb.a[3]
    obj[graph.n].a[4]=obb.a[4]
    obj[graph.n].a[5]=obb.a[5]
    obj[graph.n].a[6]=obb.a[6]
    obj[graph.n].a[7]=obb.a[7]
    obj[graph.n].a[8]=obb.a[8]
    obj[graph.n].a[9]=obb.a[9]
    obj[graph.n].b=obb.b'''

        
        
def down(obb = graph(),p = int()) :
    #print("down")
    '''test=0
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=obj[p].a[1]
    obj[graph.n].a[2]=obj[p].a[2]
    obj[graph.n].a[3]=obj[p].a[3]
    obj[graph.n].a[4]=obj[p].a[4]
    obj[graph.n].a[5]=obj[p].a[5]
    obj[graph.n].a[6]=obj[p].a[6]
    obj[graph.n].a[7]=obj[p].a[7]
    obj[graph.n].a[8]=obj[p].a[8]
    obj[graph.n].a[9]=obj[p].a[9]
    obj[graph.n].b=obj[p].b
    print(obj[graph.n].b)
    obj[graph.n].parent = p'''
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            #y=y+1
            y=y-3
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[7]!=0 and obj[graph.n].a[8]!=0 and obj[graph.n].a[9]!=0 and check==0:
        #obj[graph.n].b=obj[graph.n]-3
        print("down")
        temp=obj[graph.n].b
        temp=temp+3
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
        '''test=1
        pp = obj[graph.n].node
        print(pp)
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        #print(obj[graph.n].b)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a[1]==1 and obj[graph.n].a[2]==3 and obj[graph.n].a[5]==2:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.c
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            #up(obj[graph.n],pp)
            #if graph.stop==0:
            left(obj[pp],pp)
            #if graph.stop==0:
            down(obj[pp],pp)
            #if graph.stop==0:
            right(obj[pp],pp)
    if test==1:
        temp=obj[graph.n].b
        temp=temp-3
        #print(obj[graph.n].a[obj[graph.n].b])
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
    obj[graph.n].a[1]=obb.a[1]
    obj[graph.n].a[2]=obb.a[2]
    obj[graph.n].a[3]=obb.a[3]
    obj[graph.n].a[4]=obb.a[4]
    obj[graph.n].a[5]=obb.a[5]
    obj[graph.n].a[6]=obb.a[6]
    obj[graph.n].a[7]=obb.a[7]
    obj[graph.n].a[8]=obb.a[8]
    obj[graph.n].a[9]=obb.a[9]
    obj[graph.n].b=obb.b'''


def right(obb = graph(),p = int()) :
    #print("right")
    '''test=0
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=obj[p].a[1]
    obj[graph.n].a[2]=obj[p].a[2]
    obj[graph.n].a[3]=obj[p].a[3]
    obj[graph.n].a[4]=obj[p].a[4]
    obj[graph.n].a[5]=obj[p].a[5]
    obj[graph.n].a[6]=obj[p].a[6]
    obj[graph.n].a[7]=obj[p].a[7]
    obj[graph.n].a[8]=obj[p].a[8]
    obj[graph.n].a[9]=obj[p].a[9]
    obj[graph.n].b=obj[p].b
    print(obj[graph.n].b)
    obj[graph.n].parent = p'''
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            #y=y+1
            y=y-1
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[3]!=0 and obj[graph.n].a[6]!=0 and obj[graph.n].a[9]!=0 and check==0:
        #obj[graph.n].b=obj[graph.n]-3
        #print(obj[graph.n].b)
        print("right")
        temp=obj[graph.n].b
        temp=temp+1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
        '''test=1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        #print(obj[graph.n].b)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a[1]==1 and obj[graph.n].a[2]==3 and obj[graph.n].a[5]==2:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.c
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            print("updationnnnnn")
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                down(obj[pp],pp)
            if graph.stop==0:
                up(obj[pp],pp)
            if graph.stop==0:
                right(obj[pp],pp)
    if test==1:
        temp=obj[graph.n].b
        temp=temp-1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        pp = obj[graph.n].node
    obj[graph.n].a[1]=obb.a[1]
    obj[graph.n].a[2]=obb.a[2]
    obj[graph.n].a[3]=obb.a[3]
    obj[graph.n].a[4]=obb.a[4]
    obj[graph.n].a[5]=obb.a[5]
    obj[graph.n].a[6]=obb.a[6]
    obj[graph.n].a[7]=obb.a[7]
    obj[graph.n].a[8]=obb.a[8]
    obj[graph.n].a[9]=obb.a[9]
    obj[graph.n].b=obb.b'''


def left(obb = graph(),p = int()) :
    #print("left")
    '''test=0
    #graph.n = obb.node
    print(p)
    graph.n = graph.n+1
    print(graph.n)
    obj[graph.n] = graph()
    obj[graph.n].node = graph.n
    obj[graph.n].a[1]=obj[p].a[1]
    obj[graph.n].a[2]=obj[p].a[2]
    obj[graph.n].a[3]=obj[p].a[3]
    obj[graph.n].a[4]=obj[p].a[4]
    obj[graph.n].a[5]=obj[p].a[5]
    obj[graph.n].a[6]=obj[p].a[6]
    obj[graph.n].a[7]=obj[p].a[7]
    obj[graph.n].a[8]=obj[p].a[8]
    obj[graph.n].a[9]=obj[p].a[9]
    obj[graph.n].b=obj[p].b
    print(obj[graph.n].b)
    obj[graph.n].parent = p'''
    check=0
    size=len(graph.lock)
    if(size!=0):
        for i in range(size):
            y=graph.lock[i]
            #y=y+1
            y=y+1
            if(y>0):
                if obj[graph.n].a[y]==0:
                    check=1
    if obj[graph.n].a[1]!=0 and obj[graph.n].a[4]!=0 and obj[graph.n].a[7]!=0 and check==0:
        #obj[graph.n].b=obj[graph.n]-3
        #print(obj[graph.n].b
        print("left")
        temp=obj[graph.n].b
        temp=temp-1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
        print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
        '''test=1
        pp = obj[graph.n].node
        temp = []
        temp = [obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9]]
        print(temp)
        #print(obj[graph.n].b)
        check = 0
        for i in graph.visited:
            if graph.visited[i] == temp:
                check = 1
        if obj[graph.n].a[1]==1 and obj[graph.n].a[2]==3 and obj[graph.n].a[5]==2:
            #check =1
            print("done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            graph.target=graph.c
            graph.stop=1
        #print(obj[graph.n].a1)
        #print(obj[graph.n].b1)
        #print(obj[graph.n].a2)
        #print(obj[graph.n].b2)
        if check == 0  :
            #visited = {}
            graph.c = graph.c+1
            graph.visited[graph.c] = []
            graph.visited[graph.c].append(obj[graph.n].a[1])
            graph.visited[graph.c].append(obj[graph.n].a[2])
            graph.visited[graph.c].append(obj[graph.n].a[3])
            graph.visited[graph.c].append(obj[graph.n].a[4])
            graph.visited[graph.c].append(obj[graph.n].a[5])
            graph.visited[graph.c].append(obj[graph.n].a[6])
            graph.visited[graph.c].append(obj[graph.n].a[7])
            graph.visited[graph.c].append(obj[graph.n].a[8])
            graph.visited[graph.c].append(obj[graph.n].a[9])
            #print("updated ")
            #print(graph.visited)
            #graph.visited[graph.c].append(obj[n].b)
            #print("test")
            #twoMB(obj[graph.n],pp)
            if graph.stop==0:
                up(obj[pp],pp)
            if graph.stop==0:
                down(obj[pp],pp)
            if graph.stop==0:
                left(obj[pp],pp)
    if test==1:
        temp=obj[graph.n].b
        temp=temp+1
        obj[graph.n].a[obj[graph.n].b]=obj[graph.n].a[temp]
        obj[graph.n].a[temp]=0
        obj[graph.n].b=temp
    obj[graph.n].a[1]=obb.a[1]
    obj[graph.n].a[2]=obb.a[2]
    obj[graph.n].a[3]=obb.a[3]
    obj[graph.n].a[4]=obb.a[4]
    obj[graph.n].a[5]=obb.a[5]
    obj[graph.n].a[6]=obb.a[6]
    obj[graph.n].a[7]=obb.a[7]
    obj[graph.n].a[8]=obb.a[8]
    obj[graph.n].a[9]=obb.a[9]
    obj[graph.n].b=obb.b'''

def lock(index = int()):
    graph.lock.append(index)

def unlock():
    graph.lock.pop()
    
obj = {}
graph.n = graph.n+1
obj[graph.n] = graph()
obj[graph.n].node=graph.n
obj[graph.n].parent=-1
obj[graph.n].a[1]=5
obj[graph.n].a[2]=8
obj[graph.n].a[3]=3
obj[graph.n].a[4]=4
obj[graph.n].a[5]=6
obj[graph.n].a[6]=7
obj[graph.n].a[7]=1
obj[graph.n].a[8]=2
obj[graph.n].a[9]=0
obj[graph.n].b=9

#up(obj[graph.n],0)
#down(obj[graph.n],0)
#right(obj[graph.n],0)
#left(obj[graph.n],0)
#print(graph.visited)
#print(graph.target)
#graph.n=graph.target+1
#print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
#graph.n=graph.target
#print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
'''final =int()
for i in range(graph.c):
    if graph.visited[i]==goal:
        final = i
        break
graph.n=final
print(final)
#graph.n=graph.target
obj[graph.n].a[1]==1
#print(obj[7].parent)
#print(obj[7].a1,obj[7].b1,obj[7].a2,obj[7].b2)
while obj[graph.n].parent != -1 :
    print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])
    graph.n=obj[graph.n].parent
    print(graph.n)
print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])'''
up()
up()
left()
left()
#y=0
#lock(1)
temp=int()

#print(obj[graph.n].a[1])
y=1
for i in range(9):
    if obj[graph.n].a[y]==1:
        temp=y
    y=y+1
print(graph.lock)
#temp=6
#print("   ")
print(temp)
print("firsttttt")
if temp==1:
    print("")
if temp==2:
    right()
if temp==3:
    right()
    right()
    down()
    left()
    left()
    up()
    right()
if temp==4:
    down()
if temp==5:
    down()
    right()
    up()
    left()
    down()
if temp==6:
    down()
    right()
    right()
    up()
    left()
    left()
    down()
    right()
    up()
    left()
    down()

if temp==7:
    down()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==8:
    down()
    right()
    down()
    left()
    up()
    right()
    up()
    left()
    down()
if temp==9:
    down()
    right()
    right()
    down()
    left()
    up()
    right()
    down()
    left()
    left()
    up()
    right()
    up()
    left()
    down()
    
lock(1)
right()
right()
up()
up()
left()
left()
y=1
for i in range(9):
    if obj[graph.n].a[y]==3:
        temp=y
    y=y+1
print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])   
print("yesyesyes")
print(y)
#temp=y
print("seconddddd")
if temp==3 :
    right()
if temp==4:
    down()
    left()
    down()
    right()
    right()
    up()
    up()
    left()
    down()
if temp==5:
    down()
if temp==6:
    down()
    right()
    up()
    left()
    down()
if temp==7:
    down()
    down()
    left()
    up()
    right()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==8:
    down()
    down()
    right()
    up()
    up()
    left()
    down()
if temp==9:
    down()
    right()
    down()
    left()
    up()
    right()
    up()
    left()
    down()
    
#lock(2)
right()
right()
up()
up()

y=1
for i in range(9):
    if obj[graph.n].a[y]==2:
        temp=y
    y=y+1
print(temp)
print("thirdddddddd")
if temp==6:
    #unlock(2)
    left()
    down()
    down()
    right()
    up()
    left()
    up()
    right()
    down()
    down()
    left()
    up()
    right()
if temp==4:
    down()
    left()
    left()
if temp==5:
    print('')
if temp==7:
    down()
    down()
    left()
    left()
    up()
    right()
    down()
if temp==8:
    down()
    left()
    down()
if temp==9:
    down()
    down()
    left()
    up()
    right()
lock(2)
lock(5)
down()
right()
right()
up()
up()
unlock()
unlock()
left()
down()
lock(2)
lock(3)


left()
left()
up()
up()
y=1
for i in range(9):
    if obj[graph.n].a[y]==4:
        temp=y
    y=y+1

print(temp)
#temp=y
print("fourthhhhhh")
if temp==5:
    right()
if temp==6:
    right()
    right()
    down()
    left()
    left()
    up()
    right()
if temp==7:
    down()
if temp==8:
    right()
    down()
    left()
    up()
    right()
if temp==9:
    right()
    right()
    down()
    left()
    up()
    right()
    down()
    left()
    left()
    up()
    right()
lock(4)
down()
left()
left()

y=1
for i in range(9):
    if obj[graph.n].a[y]==5:
        temp=y
    y=y+1
#temp=y
print(temp)
print("fifthhhhhh")
if temp==5:
    print("")
if temp==6:
    right()
    up()
    right()
if temp==8:
    unlock()
    up()
    right()
    down()
    right()
    up()
    left()
    left()
    down()
    right()
    up()
    right()
    lock(4)
if temp==9:
    right()
    right()
    up()
    left()
    down()
#lock(4)
lock(5)
down()
left()
left()
unlock()
unlock()
print(graph.lock)
up()
right()

while obj[graph.n].a[6]!=6:
    down()
    right()
    up()
    left()
left()
down()
right()
right()

print(obj[graph.n].a[1] , obj[graph.n].a[2],obj[graph.n].a[3],obj[graph.n].a[4],obj[graph.n].a[5],obj[graph.n].a[6] , obj[graph.n].a[7],obj[graph.n].a[8],obj[graph.n].a[9])   
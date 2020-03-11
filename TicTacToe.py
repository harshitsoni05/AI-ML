# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:13:30 2020

@author: user
"""
import random
fir=input("Do you want to start ? ||| 1-Yes/0-No")  
  
def score(temp):
    sc=0
    if temp[0]=='o' and temp[1]=='o' and temp[2]=='o':
        sc=-1
    if temp[3]=='o' and temp[4]=='o' and temp[5]=='o':
        sc=-1
    if temp[6]=='o' and temp[7]=='o' and temp[8]=='o':
        sc=-1
    if temp[0]=='o' and temp[3]=='o' and temp[6]=='o':
        sc=-1
    if temp[1]=='o' and temp[4]=='o' and temp[7]=='o':
        sc=-1
    if temp[2]=='o' and temp[5]=='o' and temp[8]=='o':
        sc=-1
    if temp[0]=='o' and temp[4]=='o' and temp[8]=='o':
        sc=-1
    if temp[2]=='o' and temp[4]=='o' and temp[6]=='o':
        sc=-1
    if temp[0]=='x' and temp[1]=='x' and temp[2]=='x':
        sc=1
    if temp[3]=='x' and temp[4]=='x' and temp[5]=='x':
        sc=1
    if temp[6]=='x' and temp[7]=='x' and temp[8]=='x':
        sc=1
    if temp[0]=='x' and temp[3]=='x' and temp[6]=='x':
        sc=1
    if temp[1]=='x' and temp[4]=='x' and temp[7]=='x':
        sc=1
    if temp[2]=='x' and temp[5]=='x' and temp[8]=='x':
        sc=1
    if temp[0]=='x' and temp[4]=='x' and temp[8]=='x':
        sc=1
    if temp[2]=='x' and temp[4]=='x' and temp[6]=='x':
        sc=1
    return sc

def first(li,a):
    if li[a][0]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][9],li[a][1],li[a][2],li[a][3],li[a][4],li[a][5],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
    
def second(li,a):
    if li[a][1]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][9],li[a][2],li[a][3],li[a][4],li[a][5],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def third(li,a):
    if li[a][2]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][9],li[a][3],li[a][4],li[a][5],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def fourth(li,a):
    if li[a][3]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][9],li[a][4],li[a][5],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def fifth(li,a):
    if li[a][4]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][3],li[a][9],li[a][5],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def sixth(li,a):
    if li[a][5]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][3],li[a][4],li[a][9],li[a][6],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def seventh(li,a):
    if li[a][6]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][3],li[a][4],li[a][5],li[a][9],li[a][7],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def eighth(li,a):
    if li[a][7]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][3],li[a][4],li[a][5],li[a][6],li[a][9],li[a][8],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)
        
def ninth(li,a):
    if li[a][8]==0:
        if li[a][9]=='x':
            turn='o'
        else:
            turn='x'
        temp=[li[a][0],li[a][1],li[a][2],li[a][3],li[a][4],li[a][5],li[a][6],li[a][7],li[a][9],turn,a]
        sc=score(temp)
        if sc!=0:
            for z in range(9):
                if temp[z]==0:
                    if sc==-1:
                        temp[z]='o'
                    else:
                        temp[z]='x'
        temp.append(sc)
        temp.append(0)
        li.append(temp)

test=0
if fir=='0':
    li=[[0,0,0,0,0,0,0,0,0,'x',-1,0,0]]
    inp=[0,0,0,0,0,0,0,0,0,'x',-1,0,0]
else:
    li=[[0,0,0,0,0,0,0,0,0,'o',-1,0,0]]
    inp=[0,0,0,0,0,0,0,0,0,'o',-1,0,0]
a=0
for i in range(422074):
    first(li,a)
    second(li,a)
    third(li,a)
    fourth(li,a)
    fifth(li,a)
    sixth(li,a)
    seventh(li,a)
    eighth(li,a)
    ninth(li,a)
    a=a+1
i=549945
while i>=0:
    x=li[i][10]
    mn=1
    mx=-1
    c1=0
    c2=0
    n=i
    while li[i][10]==x:
        if li[i][11]<mn:
            mn=li[i][11]
            c1=c1+1
        if li[i][11]>mx:
            mx=li[i][11]
            c2=c2+1
        i=i-1
    while n!=i:
        if li[n][11]==mn:
            c1=c1+1
        if li[n][11]==mx:
            c2=c2+1
        n=n-1
    if li[x][9]=='o':
        li[x][11]=mn
        li[x][12]=c1
    else:
        li[x][11]=mx
        li[x][12]=c2

while 1:
    if inp[0]==0 or inp[1]==0 or inp[2]==0 or inp[3]==0 or inp[4]==0 or inp[5]==0 or inp[6]==0 or inp[7]==0 or inp[8]==0:
        if fir=='0':
            mx=-1
            wi=[]
            l=[]
            q=[]
            for i in range(0, 549945):
                if li[i][0]==inp[0] and li[i][1]==inp[1] and li[i][2]==inp[2] and  li[i][3]==inp[3] and li[i][4]==inp[4] and li[i][5]==inp[5] and li[i][6]==inp[6] and li[i][7]==inp[7] and li[i][8]==inp[8]:
                    z=i
            for i in range(0, 549945):
                if li[i][10]==z:
                  wi.append(li[i])
            for i in wi:
                if i[11]>mx:
                    mx=i[11]
            for i in wi:
                if i[11]==mx:
                    q.append(i)
            mn=10
            for i in q:
                if i[12]<mn:
                    mn=i[12]
                    l.append(i)
            ind=random.randint(0,len(l)-1)
            inp=l[ind]
            print(inp[0],'|',inp[1],'|',inp[2])
            print('---------')
            print(inp[3],'|',inp[4],'|',inp[5])
            print('---------')
            print(inp[6],'|',inp[7],'|',inp[8])
            print(" ")
            if len(wi)==1:
                if inp[11]==0:
                    print("Match Drawn")
                if inp[11]==1:
                    print("BOT Won")
                if inp[11]==-1:
                    print("You Won!!")
                break
            s=input("Now enter your choice(1-9) ")
            ch=int(s,10)
            ch=ch-1
            inp[ch]='o'
        else:
            s=input("Now enter your choice(1-9) ")
            ch=int(s,10)
            ch=ch-1
            inp[ch]='o'
            mx=-1
            wi=[]
            l=[]
            q=[]
            for i in range(0, 549945):
                if li[i][0]==inp[0] and li[i][1]==inp[1] and li[i][2]==inp[2] and  li[i][3]==inp[3] and li[i][4]==inp[4] and li[i][5]==inp[5] and li[i][6]==inp[6] and li[i][7]==inp[7] and li[i][8]==inp[8]:
                    z=i
            for i in range(0, 549945):
                if li[i][10]==z:
                  wi.append(li[i])
            for i in wi:
                if i[11]>mx:
                    mx=i[11]
            for i in wi:
                if i[11]==mx:
                    q.append(i)
            mn=10
            for i in q:
                if i[12]<mn:
                    mn=i[12]
                    l.append(i)
            if len(l)!=0:
                ind=random.randint(0,len(l)-1)
                inp=l[ind]
            print(inp[0],'|',inp[1],'|',inp[2])
            print('---------')
            print(inp[3],'|',inp[4],'|',inp[5])
            print('---------')
            print(inp[6],'|',inp[7],'|',inp[8])
            print(" ")
            if len(wi)==1:
                if inp[11]==0:
                    print("Match Drawn")
                if inp[11]==1:
                    print("BOT Won")
                if inp[11]==-1:
                    print("You Won!!")
                break
    else:
        break
#print(li[586])
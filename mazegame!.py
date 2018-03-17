import pygame
import sys
import random
from pygame.locals import *
from pygame import *
pygame.init()
class linkedlist:
    class node:
        def __init__(self,a,b):
            self.x=a
            self.y=b
            self.next=None
    def __init__(self):
        self.head=None
        self.trav=self.head
        self.size=0
    def insert(self,a,b):
        if self.size==0:
            self.head=self.node(a,b)
            self.size=self.size+1
            self.trav=self.head
        else:
            temp=self.head
            self.head=self.node(a,b)
            self.head.next=temp
            self.size=self.size+1
            self.trav=self.head
    def check(self,a,b):
        if self.trav.x==a and self.trav.y==b:
            if self.trav.next!=None:
                self.trav=self.trav.next
                print "right move"
                return True
            else:
                print "you won!"
                displaychange1()
        else:
            return False
l2=linkedlist()
l2.insert(9,0)
l2.insert(9,1)
l2.insert(9,2)
l2.insert(8,2)
l2.insert(7,2)
l2.insert(7,1)
l2.insert(7,0)
l2.insert(6,0)
l2.insert(5,0)
l2.insert(4,0)
l2.insert(3,0)
l2.insert(2,0)
l2.insert(1,0)
l2.insert(0,0)
l2.insert(0,1)
l2.insert(0,2)
l2.insert(1,2)
l2.insert(2,2)
l2.insert(3,2)
l2.insert(4,2)
l2.insert(5,2)
l2.insert(5,3)
l2.insert(5,4)
l2.insert(5,5)
l2.insert(5,6)
l2.insert(4,6)
l2.insert(3,6)
l2.insert(3,5)
l2.insert(2,5)
l2.insert(1,5)
l2.insert(1,6)
l2.insert(1,7)
l2.insert(2,7)
l2.insert(2,8)
l2.insert(2,9)
l2.insert(1,9)
l1=linkedlist()
l1.insert(9,0)
l1.insert(8,0)
l1.insert(7,0)
l1.insert(6,0)
l1.insert(5,0)
l1.insert(4,0)
l1.insert(3,0)
l1.insert(3,1)
l1.insert(3,2)
l1.insert(4,2)
l1.insert(5,2)
l1.insert(6,2)
l1.insert(6,3)
l1.insert(6,4)
l1.insert(7,4)
l1.insert(7,5)
l1.insert(7,6)
l1.insert(6,6)
l1.insert(5,6)
l1.insert(5,5)
l1.insert(4,5)
l1.insert(3,5)
l1.insert(3,6)
l1.insert(2,6)
l1.insert(1,6)
l1.insert(1,7)
l1.insert(1,8)
l1.insert(0,8)
l3=linkedlist()
l3.insert(9,0)
l3.insert(8,0)
l3.insert(7,0)
l3.insert(7,1)
l3.insert(7,2)
l3.insert(8,2)
l3.insert(9,2)
l3.insert(9,3)
l3.insert(9,4)
l3.insert(9,5)
l3.insert(8,5)
l3.insert(7,5)
l3.insert(7,6)
l3.insert(7,7)
l3.insert(6,7)
l3.insert(5,7)
l3.insert(4,7)
l3.insert(4,6)
l3.insert(4,5)
l3.insert(4,4)
l3.insert(4,3)
l3.insert(3,3)
l3.insert(2,3)
l3.insert(1,3)
l3.insert(0,3)
l3.insert(0,4)
l3.insert(0,5)
l3.insert(1,5)
l3.insert(2,5)
l3.insert(2,6)
l3.insert(2,7)
l3.insert(1,7)
l3.insert(0,7)
l3.insert(0,8)
l4=linkedlist()
l4.insert(9,0)
l4.insert(8,0)
l4.insert(7,0)
l4.insert(7,1)
l4.insert(7,2)
l4.insert(6,2)
l4.insert(5,2)
l4.insert(5,1)
l4.insert(4,1)
l4.insert(3,1)
l4.insert(2,1)
l4.insert(1,1)
l4.insert(0,1)
l4.insert(0,2)
l4.insert(0,3)
l4.insert(0,4)
l4.insert(1,4)
l4.insert(2,4)
l4.insert(2,3)
l4.insert(3,3)
l4.insert(4,3)
l4.insert(4,4)
l4.insert(4,5)
l4.insert(5,5)
l4.insert(6,5)
l4.insert(6,6)
l4.insert(7,6)
l4.insert(8,6)
l4.insert(8,7)
l4.insert(8,8)
l4.insert(7,8)
l4.insert(6,8)
l4.insert(6,9)
l4.insert(5,9)
l4.insert(4,9)
l4.insert(4,8)
l4.insert(4,7)
l4.insert(3,7)
l4.insert(2,7)
l4.insert(2,8)
l4.insert(2,9)
l4.insert(1,9)
l5=linkedlist()
l5.insert(9,0)
l5.insert(9,1)
l5.insert(9,2)
l5.insert(8,2)
l5.insert(7,2)
l5.insert(7,1)
l5.insert(7,0)
l5.insert(6,0)
l5.insert(5,0)
l5.insert(4,0)
l5.insert(3,0)
l5.insert(2,0)
l5.insert(1,0)
l5.insert(1,1)
l5.insert(1,2)
l5.insert(2,2)
l5.insert(3,2)
l5.insert(4,2)
l5.insert(5,2)
l5.insert(5,3)
l5.insert(5,4)
l5.insert(6,4)
l5.insert(7,4)
l5.insert(7,5)
l5.insert(7,6)
l5.insert(6,6)
l5.insert(6,7)
l5.insert(6,8)
l5.insert(5,8)
l5.insert(4,8)
l5.insert(4,7)
l5.insert(4,6)
l5.insert(4,5)
l5.insert(3,5)
l5.insert(2,5)
l5.insert(2,6)
l5.insert(1,6)
l5.insert(0,6)
l5.insert(0,7)
l5.insert(0,8)
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,51))
display.flip()
def displaychange():
    font = pygame.font.Font(None, 36)
    text=font.render("WRONG MOVE! GAME OVER!",1,(0,0,0))
    box3=Rect(0,100,300,200)
    screen.blit(text,box3)
    display.flip()
    t=time.get_ticks()
    while time.get_ticks()<t+4000:
        o=1
    pygame.display.quit()
    sys.exit()
def displaychange1():
    font = pygame.font.Font(None, 36)
    text=font.render("CONGRATULATIONS! YOU WON!",1,(0,0,0))
    box3=Rect(0,100,300,200)
    screen.blit(text,box3)
    display.flip()
    t=time.get_ticks()
    while time.get_ticks()<t+4000:
        o=1
    pygame.display.quit()
    sys.exit()
def displaychange2():
    font = pygame.font.Font(None, 36)
    text=font.render("TIME UP! GAME OVER",1,(0,0,0))
    box3=Rect(0,100,300,200)
    screen.blit(text,box3)
    display.flip()
    t=time.get_ticks()
    while time.get_ticks()<t+4000:
        o=1
    pygame.display.quit()
    sys.exit()
def displaychange3():
    font = pygame.font.Font(None, 50)
    text=font.render("        MAZE GAME",1,(0,0,0))
    box3=Rect(0,100,300,50)
    screen.blit(text,box3)
    display.flip()
    font = pygame.font.Font(None, 25)
    text=font.render("RULES: Use the arrow keys and solve through ",1,(0,0,0))
    box3=Rect(0,160,300,50)
    screen.blit(text,box3)
    display.flip()
    font = pygame.font.Font(None, 25)
    text=font.render("the maze within the time limit(10 secs)",1,(0,0,0))
    box3=Rect(0,200,300,50)
    screen.blit(text,box3)
    display.flip()
a2=[[1,1,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,1,0,1],[1,1,1,1,1,1,0,1,1,1],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,1,1,1,0,1,0,0,0,0],[0,1,0,1,1,1,0,0,0,0],[0,1,1,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0]]
a1=[[0,0,0,1,1,1,1,1,1,1],[0,0,0,1,0,0,0,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,1,0,0],[0,0,0,1,1,1,0,1,0,0],[0,1,1,1,0,1,1,1,0,0],[0,1,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0]]
a3=[[0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1],[1,1,1,1,1,0,0,0,0,1],[1,0,0,0,1,0,0,0,0,1],[1,1,1,0,1,0,0,1,1,1],[0,0,1,0,1,0,0,1,0,0],[1,1,1,0,1,1,1,1,0,0],[1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0]]
a4=[[0,0,0,0,0,0,0,1,1,1],[1,1,1,1,1,1,0,1,0,0],[1,0,0,0,0,1,1,1,0,0],[1,0,1,1,1,0,0,0,0,0],[1,1,1,0,1,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,1,1,1,0],[0,0,1,1,1,0,0,0,1,0],[0,0,1,0,1,0,1,1,1,0],[1,1,1,0,1,1,1,0,0,0]]
a5=[[0,1,1,1,1,1,1,1,0,1],[0,1,0,0,0,0,0,1,0,1],[0,1,1,1,1,1,0,1,1,1],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,1,1,0,0],[0,0,1,1,1,0,0,1,0,0],[1,1,1,0,1,0,1,1,0,0],[1,0,0,0,1,0,1,0,0,0],[1,0,0,0,1,1,1,0,0,0],[1,0,0,0,0,0,0,0,0,0]]
array=[]
array.append(a1)
array.append(a2)
array.append(a3)
array.append(a4)
array.append(a5)
answer=[]
answer.append(l1)
answer.append(l2)
answer.append(l3)
answer.append(l4)
answer.append(l5)
t1=time.get_ticks()
displaychange3()
while time.get_ticks()<t1+5000:
    o=1    
r=random.randint(-1,4)
a=array[r]
l=answer[r]
i=0
j=0
x=0
y=0
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=1
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=2
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=3
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40

i=4
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=5
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=6
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=7
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=8
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
i=9
j=0
x=0
y=y+40
while j<10:
    if a[i][j]==0:
        box=Rect(x,y,40,40)
        draw.rect(screen,(255,0,0),box,0)
    else:
        box=Rect(x,y,40,40)
        draw.rect(screen,(0,0,255),box,0)
    display.flip()
    j=j+1
    x=x+40
going=True
c=0
b=360
box1=Rect(c,b,40,40)
draw.rect(screen,(0,255,0),box1,0)
display.flip()
k=9
p=0
while going and time.get_ticks()<t1+16000:
    for e in event.get():
        if e.type==KEYDOWN:
            if e.key==K_DOWN:
                c=c
                b=b+40
                p=p
                k=k+1
                if c>=0 and c<=360 and b>=0 and b<=360:
                    box1=Rect(c,b-40,40,40)
                    draw.rect(screen,(0,0,255),box1,0)
                    display.flip()
                    box1=Rect(c,b,40,40)
                    draw.rect(screen,(0,255,0),box1,0)
                    display.flip()
                    if l.check(p,k)==False:
                        print "wrong move1"
                        displaychange()
                        going=False
                else:
                    print "wrong move"
                    print "game over"
                    displaychange()
                    going=False
            if e.key==K_UP:
                c=c
                b=b-40
                p=p
                k=k-1
                if c>=0 and c<=360 and b>=0 and b<=360:
                    box1=Rect(c,b+40,40,40)
                    draw.rect(screen,(0,0,255),box1,0)
                    display.flip()
                    box1=Rect(c,b,40,40)
                    draw.rect(screen,(0,255,0),box1,0)
                    display.flip()
                    if l.check(p,k)==False:
                        print "wrong move1"
                        displaychange()
                        going=False
                else:
                    print "wrong move"
                    displaychange()
                    going=False
            if e.key==K_RIGHT:
                c=c+40
                b=b
                p=p+1
                k=k
                if c>=0 and c<=360 and b>=0 and b<=360:
                    box1=Rect(c-40,b,40,40)
                    draw.rect(screen,(0,0,255),box1,0)
                    display.flip()
                    box1=Rect(c,b,40,40)
                    draw.rect(screen,(0,255,0),box1,0)
                    display.flip()
                    if l.check(p,k)==False:
                        print "wrong move1"
                        displaychange()
                        going=False
                else:
                    print "wrong move"
                    displaychange()
                    going=False
            if e.key==K_LEFT:
                c=c-40
                b=b
                p=p-1
                k=k
                if c>=0 and c<=360 and b>=0 and b<=360:
                    box1=Rect(c+40,b,40,40)
                    draw.rect(screen,(0,0,255),box1,0)
                    display.flip()
                    box1=Rect(c,b,40,40)
                    draw.rect(screen,(0,255,0),box1,0)
                    display.flip()
                    if l.check(p,k)==False:
                        print "wrong move1"
                        displaychange()
                        going=False
                else:
                    print "wrong move"
                    displaychange()
                    going=False
if time.get_ticks>t1+16000:
    displaychange2()
    print "time up!"
    print "game over"
                            
                    
                    
            

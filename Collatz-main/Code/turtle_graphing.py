import turtle
t = turtle.Turtle()
global export
export = []

def printPaths(root):

    path = []
    printPathsRec(root, path, 0)
    
    #global export
    #import pandas as pd   
    #df = pd.DataFrame(export)
    #df.to_csv('myfile.csv',index = False)


def printPathsRec(root, path, pathLen):
     
    # Base condition - if binary tree is
    # empty return
    if root is None:
        return
 
    # add current root's data into
    # path_ar list
     
    # if length of list is gre
    if(len(path) > pathLen):
        path[pathLen] = root.data
    else:
        path.append(root.data)
 
    # increment pathLen by 1
    pathLen = pathLen + 1
 
    if root.left is None and root.right is None:
         
        # leaf node then print the list
        printArray(path, pathLen)
    else:
        # try for left and right subtree
        printPathsRec(root.left, path, pathLen)
        printPathsRec(root.right, path, pathLen)
def printArray(ints, len):

    a = []
    for i in ints[0 : len]:
        a.append(i)
    #export.append(a)
    draw(a)


def resetPen():
    t.up()
    t.setpos(300,-300) 
    t.down()


def left():
    create_arc(t.xcor(),t.ycor(), (t.xcor())-10,(t.ycor())+10,90)

def right():
    create_arc(t.xcor(),t.ycor(), (t.xcor())+10,(t.ycor())+10,0)

def create_arc( x1, y1, x2, y2,h, start=0, extent=90):

    radius = min(abs(x2 - x1), abs(y2 - y1)) / 2
    t.speed(1000000000)
    t.penup()
    t.setposition(x1, y2-10)
    t.setheading(h)
    t.pendown()
    t.circle(7, extent=extent)

def draw(array):
    resetPen()
   
    for a in array:
        if a %2 ==0:
            left()
        else: right()


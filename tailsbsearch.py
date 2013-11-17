# hello teamates this is our file. add your code and comment your name

# Nolan English Code Follows

#TEST EDIT 2

import random

List = []

x = 10

while x >= 0:
    random.seed()
    List.append(random.randint(1,10))
    x -= 1
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
# hello teamates this is our file. add your code and comment your name
# Nolan English Code Follows
#TEST EDIT 2
import random
List = []
x = 10
while x >= 0:
    random.seed()
    List.append(random.randint(1,10))
    x -= 1
x = 10
def sorting(a,d):
    c = 0
    a.sort()
    print a
    for i in a:
        if i == d:
            c += 1
    if c == 0:
        print "the value %s is not in the list try again" % (str(d))
    elif c > 1:
        print "their is more than one instance of what you are looking for: %s" %(str(d)) 
    elif c == 1:
        b = ((len(a) - 1) / 2)
        endpoint = len(a) -1
        startpoint = 0 
        while True:
            if d >= a[b]:
                startpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
Commit summary: Extended description: (optional)
jahmaal jahmaal.gayle@bison.howard.edu

x = 10

def sorting(a,d):
    c = 0
    a.sort()
    print a
    for i in a:
        if i == d:
            c += 1
    if c == 0:
        print "the value %s is not in the list try again" % (str(d))
    elif c > 1:
        print "their is more than one instance of what you are looking for: %s" %(str(d)) 
    elif c == 1:
        b = ((len(a) - 1) / 2)
        endpoint = len(a) -1
        startpoint = 0 
        while True:
            if d >= a[b]:
                startpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" %(str(a[endpoint]),str(endpoint))
                        break
                break
            break
        while True:
            if d <= a[b]:
                endpoint = b
                while True:
                    if d > a[endpoint - ((endpoint-startpoint)/2)]:
                        startpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d < a[endpoint - ((endpoint-startpoint)/2)]:
                        endpoint = (endpoint - ((endpoint-startpoint)/2))
                    if d == a[endpoint - ((endpoint-startpoint)/2)]:
                        print "the value %s is at %s\n" % (str(a[endpoint - ((endpoint-startpoint)/2)]) ,str(endpoint - ((endpoint-startpoint)/2))) 
                        break
                    if d == a[startpoint]:
                        print "the value %s is at %s\n" % (str(a[startpoint]),str(startpoint))
                        break
                    if d == a[endpoint]:
                        print "the value %s is at %s\n" % (str(a[endpoint]),str(endpoint))
                        break
                break
            break
        if d == a[b]:
            print "wow its exactly in the middle"

while x > 0:
    sorting(List,x)
    x -=1
    


# Nolan English CODE ends



#Hey Guys: Jahmaal Gayle @02661559 CODE

def ageSearch (ages, targetAge, bottomIndexes=0, topIndexes=5):
    if topIndexes is 5:
        topIndexes = len(ages)
    while bottomIndexes < topIndexes:
        middleIndexes = (bottomIndexes+topIndexes)//2
        middleNumber = ages[middleIndexes]
        if middleNumber < targetAge:
            bottomIndexes = middleNumber+1
        elif middleNumber > targetAge:
            topIndexes = middleIndexes
        else:
            return middleIndexes
    return -1
ages=(5,10,15,20,25,30)
targetAge=20
index=ageSearch(ages, targetAge, bottomIndexes=0, topIndexes=5)
print index

#Jahmaal Gayle code ends

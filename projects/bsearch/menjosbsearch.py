#Maimuna Ahmed's code starts hur
def bsearch( alist , element):
	alist.sort()
	front = 0
	back = len(alist)-1
	found = True
	midpoint = (front + back)//2

	for i in range(len(alist)):

		if alist[midpoint] == element:
			return midpoint

		elif element > alist[midpoint]:
			front = midpoint + 1
			midpoint = (front + back)//2

		elif element < alist[midpoint]:
			back = midpoint - 1
			midpoint = (front + back)//2

	return -1
#Maimuna Ahmed's code ends hur
#Selina Jones git-jayenator565 bsearch code


def bsearch(mylist,x):
    mylist.sort()	
    size=len(mylist)
    low=0
    high=size
    if mylist==[]:
        return mylist
    if high==size:
        high =len(mylist)-1
    while low<=high:
        mid = (low+high)/2
        midval=mylist[mid]
        if midval<x:
            low=mid+1
        elif midval>x:
            high=mid
        else:
            return mid
    return -1

#Oreoluwa Onatemowo's code starts here
def bsearch(searchlist,searchElement):       
    searchlist.sort()
    length = len(searchlist)
    initial_index=0
    final_index = len(searchlist)-1
    midpoint = (initial_index + final_index)/2
    if searchlist ==[]:
        return -1
    if searchlist[midpoint] == searchElement:
        return midpoint
        pass
    while searchlist[midpoint]!=searchElement:
        if searchlist[midpoint]  < searchElement:
            initial_index = midpoint+1
            midpoint = (initial_index+final_index)/2
            length = midpoint - initial_index                  
        elif searchlist[midpoint] > searchElement:            
            final_index = midpoint-1
            midpoint=(initial_index+final_index)/2 
            length = midpoint - initial_index          
        if searchlist[midpoint] == searchElement:                
                return midpoint
        if initial_index>final_index:
                break    
    return -1


#Oreoluwa Onatemowo's code ends here

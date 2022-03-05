def srev(newlist,pos):
    if (len(newlist)==0):
        return []
    
    #Check if number at current index is a list
    if type(newlist[pos]) == list:
        newlist[pos]=srev(newlist[pos],0)
    
    #Check if next index exists. If it does, increase index and run again (Will recurse untill end of list, then collapse). If it does not, reverse and return current list.
    try:
        newlist[pos+1]
        newlist=srev(newlist,pos+1)
        return newlist

    except:
        newlist=newlist[::-1]
        return newlist

mylist=[1, [2 ,3], 4, [5, [6]]]
mylist2=[]
mylist3=[[1,2,[3,[8,[10,20,[23,88]]]]]]
mylist4=['a',['b','c',['d','e',['f','g','h']]],'i','j',['l',['m','n',['o','p',['q','r','s']]]]]
mylist5=['red','orange','yellow','green','blue','purple']

print("List1: ",mylist)
print("Reversed1: ",srev(mylist, 0))
print("List2: ",mylist2)
print("Reversed2: ",srev(mylist2, 0))
print("List3: ",mylist3)
print("Reversed3:",srev(mylist3,0))
print("List4: ",mylist4)
print("Reversed4:",srev(mylist4,0))
print("List5: ",mylist5)
print("Reversed5:",srev(mylist5,0))

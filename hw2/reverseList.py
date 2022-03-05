def reverseList(l, front, back):
    #base case 
    if (back<=front):
        return
    temp=l[front]
    l[front]=l[back]
    l[back]=temp
    reverseList(l, front+1, back-1)
    
mylist = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e']
print("Starting list 1: ",mylist)
reverseList(mylist, 0, len(mylist)-1)
print("Reversed list 1: ",mylist)

mylist2 =[]
print("Starting list 2: ",mylist2)
reverseList(mylist2, 0, len(mylist2)-1)
print("Reversed list 2: ",mylist2)

mylist3=[1,2,3]
print("Starting list 3: ",mylist3)
reverseList(mylist3, 0, len(mylist3)-1)
print("Reversed list 3: ",mylist3)

mylist4=['red','orange','yellow','green','blue','purple']
print("Starting list 3: ",mylist3)
reverseList(mylist3, 0, len(mylist3)-1)
print("Reversed list 3: ",mylist3)

mylist5=[5.8, 9.2, 2.2, 8.7]
print("Starting list 5: ",mylist5)
reverseList(mylist5, 0, len(mylist5)-1)
print("Reversed list 5: ",mylist5)

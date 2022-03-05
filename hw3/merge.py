def Merge(L1, L2):
    if L1 and L2:
        if L1[0]>L2[0]:
            return [L2[0]]+Merge(L2[1:],L1)
        return [L1[0]]+Merge(L1[1:],L2)
    return L1+L2

def MergeSort(items):
    if (len(items)<=1):  
        return items

    return Merge(MergeSort(items[:(len(items)//2)]),MergeSort(items[(len(items)//2):]))
 
# Testing for part 1c
mylist1=[]
print("Unsorted List: ",mylist1)
newlist1=MergeSort(mylist1)
print("Sorted List: ", newlist1)
print()
#L2
mylist2=[159,43,2,1,3,7,8,5,4,9,43,10,57,98,33,12]
print("Unsorted List: ",mylist2)
newlist2=MergeSort(mylist2)
print("Sorted List: ", newlist2)
print()
#L3
mylist1=[33,77,93,35,16,32,45,91,2,20,60,71,100,55,73]
print("Unsorted List: ",mylist1)
newlist1=MergeSort(mylist1)
print("Sorted List: ", newlist1)
print()
#L4
mylist4=[10,9,8,7,6,5,4,3,2,1]
print("Unsorted List: ",mylist4)
newlist4=MergeSort(mylist4)
print("Sorted List: ", newlist4)
print()
#L5
mylist5=[100,98,77,21,-500]
print("Unsorted List: ",mylist5)
newlist5=MergeSort(mylist5)
print("Sorted List: ", newlist5)
print()
#L6 
mylist6=[-6,-8,-49,-80,-31,-97,-44,-98,-74,-95,84,-26,50,2,65,-62,-28,16,-94,60,72]
print("Unsorted List: ",mylist6)
newlist6=MergeSort(mylist6)
print("Sorted List: ", newlist6)
print()
#L7 
mylist7=[14.74,53.44,-49.19,-24.68,-83.66,-43.26,-30.34,-52.73,57.29,73.34,-29.8,21.07,-43.84]
print("Unsorted List: ",mylist7)
newlist7=MergeSort(mylist7)
print("Sorted List: ", newlist7)
print()
#L8
mylist8=[99.56,-54.59,-61.4,22.04,-66.98,92.24,36.87,-49.66]
print("Unsorted List: ",mylist8)
newlist8=MergeSort(mylist8)
print("Sorted List: ", newlist8)

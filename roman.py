#takes two lists returns false if term2 can't be subtracted from term2
def validSub(term1,term2):
  #cant have two of the same number because no zero representation
  if(term1==term2):
    return False

  unCompact(term1)
  unCompact(term2)

  countM, countD, countC, countL, countX, countV, countI=countNums(term1)
  countM2, countD2, countC2, countL2, countX2, countV2, countI2=countNums(term2)

  if countM2>countM:
    return False
  elif countD2>countD:
    return False
  elif countC2>countC:
    return False
  elif countL2>countL:
    return False
  elif countX2>countX:
    return False
  elif countV2>countV:
    return False
  elif countI2>countI:
    return False

  return True

#returns if a roman numeral is valid when a term is passed to it as a list
def validNum(term):
   countM, countD, countC, countL, countX, countV, countI=countNums(term)

   #V, L, D sould not be repeated at all
   if countD>1 or countL>1 or countV>1:
     return False
   #There should never be more than 4 of the same letter
   if countC>4 or countX>4 or countI>4:
     return False

   return True

# a function that splits the input into five seperate variables to be stored
def getInput():
  equation = input().split()  #split stores everything in between spaces as a list
  term1 = equation[0]
  op1 = equation[1][0] #gets the first character of the second list item
  term2 = equation[2]
  if len(equation)>3: #if three terms take all three else just take two
    op2 = equation[3][0]
    term3 = equation[4]
    return term1, op1, term2, op2, term3
  else:
    return term1, op1, term2, "", ""

  def unCompact(term):
  subs=["IV","IX","XL","XC","CD","CM"]
  size=len(term)-1
  subssize=len(subs)

  str=""
  temp=[]

  for i in range(size): #gets sets of two characters from term
    j=i+1
    str=""
    str+=term[i]
    str+=term[j]

    #k is current pos of subs list
    for k in range(subssize):
      if str==subs[k]:
        if k%2==1: #if odd pos in subs then have to add a five too
          temp.append(subs[(k-1)][1])
        for l in range(4):
          temp.append(subs[k][0])
        term.pop(i)
        term.pop(i) #when i pop i thats gonna change pos j to be i
        size -= 2
    if (i>size-1): #dont let loop go out of list bounds
      break
  term+=temp

  #compacts subtractives and stores resullt in original list
def compact(term):
  size4=len(term)-3
  size5=len(term)-4
  pos=-1

  #check for subtractives of four of the same characters
  for i in range(size4):
     if term[i]=='I' and term[i+1]=='I' and term[i+2]=='I' and term[i+3]=='I':
       pos=term.index('I')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'I')
       term.insert(pos+1,'V')
  for i in range(size4):
     if term[i]=='X' and term[i+1]=='X' and term[i+2]=='X' and term[i+3]=='X':
       pos=term.index('X')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'X')
       term.insert(pos+1,'L')
  for i in range(size4):
     if term[i]=='C' and term[i+1]=='C' and term[i+2]=='C' and term[i+3]=='C':
       pos=term.index('C')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'C')
       term.insert(pos+1,'D')

  #check for subtractives of one character followed by four repeating characters
  for i in range(size5):
     if term[i]=='V' and term[i+1]=='I' and term[i+2]=='I' and term[i+3]=='I' and term[i+4]=='I':
       pos=term.index('V')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'I')
       term.insert(pos+1,'X')

  for i in range(size5):
     if term[i]=='L' and term[i+1]=='X' and term[i+2]=='X' and term[i+3]=='X' and term[i+4]=='X':
       pos=term.index('L')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'X')
       term.insert(pos+1,'C')

  for i in range(size5):
     if term[i]=='D' and term[i+1]=='C' and term[i+2]=='C' and term[i+3]=='C' and term[i+4]=='C':
       pos=term.index('C')
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.pop(pos)
       term.insert(pos,'C')
       term.insert(pos+1,'M')

#count the number of each roman numeral in a list and return these values
def countNums(l):
  countM=l.count('M')
  countD=l.count('D')
  countC=l.count('C')
  countL=l.count('L')
  countX=l.count('X')
  countV=l.count('V')
  countI=l.count('I')

  return countM, countD, countC, countL, countX, countV, countI

#Sort a list of roman numerals from high to low
def sortNums(l, countM, countD, countC, countL, countX, countV, countI):
  l.clear()

  for i in range(countM):
    l.append('M')
  for i in range(countD):
    l.append('D')
  for i in range(countC):
    l.append('C')
  for i in range(countL):
    l.append('L')
  for i in range(countX):
    l.append('X')
  for i in range(countV):
    l.append('V')
  for i in range(countI):
    l.append('I')

#if a group of the same letter can be reduced to a bigger letter then reduce it
def groupNums(l, countM, countD, countC, countL, countX, countV, countI):
   pos=-1

   if countD>=2:
     countD-=2
     pos=l.index('D')
     l.pop(pos)
     l.pop(pos)
     l.insert(pos,'M')
   if countC>=10:
     countC-=10
     pos=l.index('C')
     for i in range(10):
       l.pop(pos)
     l.insert(pos,'M')
   if countC>=5:
     countC-=5
     pos=l.index('C')
     for i in range(5):
       l.pop(pos)
     l.insert(pos,'D')
   if countL>=20:
     countL-=20
     pos=l.index('L')
     for i in range(20):
       l.pop(pos)
     l.insert(pos,'M')
   if countL>=10:
     countL-=10
     pos=l.index('L')
     for i in range(10):
       l.pop(pos)
     l.insert(pos,'D')
   if countL>=2:
     countL-=2
     pos=l.index('L')
     l.pop(pos)
     l.pop(pos)
     l.insert(pos,'C')
   if countX>=100:
     countX-=100
     pos=l.index('X')
     for i in range(100):
       l.pop(pos)
     l.insert(pos,'M')
   if countX>=50:
     countX-=50
     pos=l.index('X')
     for i in range(50):
       l.pop(pos)
     l.insert(pos,'D')
   if countX>=10:
     countX-=10
     pos=l.index('X')
     for i in range(10):
       l.pop(pos)
     l.insert(pos,'C')
   if countX>=5:
     countX-=5
     pos=l.index('X')
     for i in range(5):
       l.pop(pos)
     l.insert(pos,'L')
   if countV>=200:
     countV-=200
     pos=l.index('V')
     for i in range(200):
       l.pop(pos)
     l.insert(pos,'M')
   if countV>=100:
     countV-=100
     pos=l.index('V')
     for i in range(100):
       l.pop(pos)
     l.insert(pos,'D')
   if countV>=20:
     countV-=20
     pos=l.index('V')
     for i in range(20):
       l.pop(pos)
     l.insert(pos,'C')
   if countV>=10:
     countV-=10
     pos=l.index('V')
     for i in range(10):
       l.pop(pos)
     l.insert(pos,'L')
   if countV>=2:
     countV-=2
     pos=l.index('V')
     for i in range(2):
       l.pop(pos)
     l.insert(pos,'X')
   if countI>=1000:
     countI-=1000
     pos=l.index('I')
     for i in range(1000):
       l.pop(pos)
     l.insert(pos,'M')
   if countI>=500:
     countI-=500
     pos=l.index('I')
     for i in range(500):
       l.pop(pos)
     l.insert(pos,'D')
   if countI>=100:
     countI-=100
     pos=l.index('I')
     for i in range(100):
       l.pop(pos)
     l.insert(pos,'C')
   if countI>=50:
     countI-=50
     pos=l.index('I')
     for i in range(50):
       l.pop(pos)
     l.insert(pos,'L')
   if countI>=10:
     countI-=10
     pos=l.index('I')
     for i in range(10):
       l.pop(pos)
     l.insert(pos,'X')
   if countI>=5:
     countI-=5
     pos=l.index('I')
     for i in range(5):
       l.pop(pos)
     l.insert(pos,'V')

def add(l1, l2, l3, result):
  #step 1-Uncompact Subtractive
  unCompact(l1)
  unCompact(l2)
  unCompact(l3)
  #step 2-concatenate
  result+=l1
  result+=l2
  result+=l3
  #step 3-sort
  m, d, c, L, x, v, i=countNums(result)
  sortNums(result, m, d, c, L, x, v, i)
  #step 4-group nums
  groupNums(result, m, d, c, L, x, v, i)
  #step 5-compact subtractives
  compact(result)

#Delete all letters two terms have in common from both lists
def eliminate(term1, term2):
  nums=["M","D","C","L","X","V","I"]
  size=len(nums)
  pos1=-1
  pos2=-2
  for i in range(size):
    pos1=term1.index(nums[i]) if nums[i] in term1 else -1
    pos2=term2.index(nums[i]) if nums[i] in term2 else -1
    while pos1!=-1 and pos2!=-1:
      term1.pop(term1.index(nums[i]))
      term2.pop(term2.index(nums[i]))
      pos1=term1.index(nums[i]) if nums[i] in term1 else -1
      pos2=term2.index(nums[i]) if nums[i] in term2 else -1

#break the highest roman numeral in a list into smaller roman numerals
def ungroup(term):
  nums=["M","D","C","L","X","V","I"]
  size=len(nums)
  max=0
  for i in range(size-1):
    if nums[i] in term:
      if i%2==1:
        max=5
      else:
        max=2
      term.pop(term.index(nums[i]))
      for j in range(max):
        term.append(term.index(nums[i]),nums[i])
      break

def subtract(term1, term2):
  #Step 1-uncompact subtractives
  unCompact(term1)
  unCompact(term2)
  #Step 2-eliminate common symbols
  eliminate(term1, term2)
  #Steps 3&4- Ungroup and eliminate until second term gone
  while len(term2)>0:
    ungroup(term1)
    eliminate(term1,term2)
  #Step 5-compact subtractives
  compact(term1)

#print the final answer as a string instead of a list
def printAns(l):
  str="="
  for i in l:
    str+=i
  print(str)

#main--------------------------------------------
#NOWHERE CAN ROMAN NUMERALS BE CONVERTED TO INTS
#Make sure: output correct format, error message
#  for incorrectly formatted nums, error for
#  subtracting a bigger number from a smaller

onesnums=["I","X","C","M"]
fivesnums=["V","L","D"]

#these are all strings
term1, op1, term2, op2, term3 = getInput()

#turn strings into lists of characters
list1=list(term1)
list2=list(term2)
list3=list(term3)

#remove ()
if '(' in list1:
  list1.pop(list1.index('('))
if ')' in list2:
  list2.pop(list2.index(')'))

listAns=[] #used to store answer for addition

#check form of numerals
valid1=validNum(list1)
valid2=validNum(list2)
valid3=validNum(list3)

if (not valid1):
  print("The equation can't be solved because term 1 is invalid.")
elif (not valid2):
  print("The equation can't be solved because term 2 is invalid.")
elif (not valid3):
  print("The equation can't be solved because term 3 is invalid.")
else:
  if op1=="+":
    add(list1, list2, list3, listAns)
    printAns(listAns)
  else:
    if validSub(list1, list2) and validSub(list1, list3):
      subtract(list1, list2)
      subtract(list1, list3)
      printAns(list1)
    else:
      print("The first term must be bigger than the second term in order to subtract.")

import numpy as np

# a function that splits the input into three seperate variables to be stored
def getInput():
  equation = input().split()  #split stores everything in between spaces as a list
  lhs = int(equation[0])
  o = equation[1][0] #gets the first character of the second list item
  rhs = int(equation[2])
  return lhs, o, rhs

#a function that return a two d array of the basic abacus
def declare():
  matrix = np.array([['o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['-','-','-','-','-','-','-','-','-','-','-','-','-'],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
['o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o'],
['o','o','o','o','o','o','o','o','o','o','o','o','o']])
  return matrix

#a function that prints the abacus passed to it
def printAb(matrix):
  for i in matrix:
    print(' '.join(map(str,i)))

#gets every digit of a number and returns a list of them seperated
def getDigits(x):
  leng = len(str(x))
  list = []
  i=leng

  while i>0:
    temp = x // pow(10,(i-1))
    list.append(temp)
    x %= pow(10,(i-1))

    i -= 1
  return list

# Moves the next piece of the lower deck up given a certain column
def moveLowerUp(matrix, col):
  if matrix[11,col]=='o': #1st bead
    matrix[5,col]='o'
    matrix[11,col]=' '
  elif matrix[12,col]=='o': #2nd bead
    matrix[6,col]='o'
    matrix[12,col]=' '
  elif matrix[13,col]=='o': #3rd bead
    matrix[7,col]='o'
    matrix[13,col]=' '
  elif matrix[14,col]=='o': #4th bead
    matrix[8,col]='o'
    matrix[14,col]=' '
  elif matrix[15,col]=='o': # 5th bead
    matrix[5,col]=' '
    matrix[6,col]=' '
    matrix[7,col]=' '
    matrix[8,col]=' '
    matrix[14,col]='o'
    matrix[13,col]='o'
    matrix[12,col]='o'
    matrix[11,col]='o'
    if matrix[3,col]=='o':
      #5 already there
      matrix[3,col]=' '
      matrix[1,col]='o' #reset 5's
      moveLowerUp(matrix,(col-1)) #carry a 10
    else:
      matrix[1,col]=' '
      matrix[3,col]='o' #if 5 not there move a 5
  # reset condition, carry

#Turns the abacus from starting position into reperesentation
# of desired number
def setAb(digits, matrix):
  count = len(digits)
  col = 13-count

  while count>0: #go col to col left to right
   if (digits[0])>=5: #deal with 5 first
     matrix[1,col] = ' '
     matrix[3,col] = 'o'
     digits[0] -= 5
   while digits[0]>0: #add as many ones as needed
     moveLowerUp(matrix,col)
     digits[0] -= 1

   digits.pop(0)
   count -= 1
   col += 1

#adds rhs to lhs using the lhs matrix to start
def addNums(lhs, rhs, matrix):
  rhslen=len(rhs)
  rhscount=1
  rhscol=13-rhslen

  while rhscount<=rhslen: #col to col left to right
    while rhs[(rhscount-1)]>0: #move as many beads as needed
      moveLowerUp(matrix,rhscol)
      rhs[(rhscount-1)] -= 1
    rhscount += 1
    rhscol += 1

 #returns the numerical representation of an abacus picture
# (just used for checking final answer)
def finalAnswer(matrix):
  sum=0
  x=0
  while x<=12:
   if matrix[3,(12-x)]=='o':
    sum += (pow(10, x) * 5)
   if matrix[9,(12-x)]=='o':
    sum += pow(10,x)
   if matrix[8,(12-x)]=='o':
    sum += pow(10,x)
   if matrix[7,(12-x)]=='o':
    sum += pow(10,x)
   if matrix[6,(12-x)]=='o':
    sum += pow(10,x)
   if matrix[5,(12-x)]=='o':
    sum += pow(10,x)
   x += 1

  return sum

#main------------------------------------------
term1, opp, term2 = getInput()

ab_lhs = declare()
ab_rhs = declare()

setAb(getDigits(term1), ab_lhs)
setAb(getDigits(term2), ab_rhs)

print("\nTerm 1 Abacus Representation: ")
printAb(ab_lhs)
print("\nTerm 2 Abacus Representation: ")
printAb(ab_rhs)

addNums(getDigits(term1), getDigits(term2), ab_lhs)

ans=finalAnswer(ab_lhs)
print("\nResulting Abacus:  ")
printAb(ab_lhs)
print("\nSo, "+str(term1)+"+"+str(term2)+"="+str(ans))

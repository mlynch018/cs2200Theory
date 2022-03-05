import random #used for random number generation
import string

#used in n2s and s2n
def rp(alph,s):
    alen=len(alph)
    slen=len(s)
    listsize=pow(alen,slen)
    order=['']*listsize
    
    
    b=pow(alen,slen-1) #num times to consecutively pring letter 
    c=0; #pos of thing in list
    i=slen;
    
    while i>0:
        while (c<listsize):
            for a in range(0,alen):
                btemp=b
                while (btemp>=1):
                    order[c]+=alph[a]
                    c+=1
                    btemp-=1
        i-=1
        c=0
        b//=alen
    
    return order

def n2s(alph, n):
    multiple = len(alph)
    prod = 1
    s = 0 
    string = ''
    L = []
    while (s<n):
        string+='a'
        prod*=multiple 
        s+=prod
        L+=rp(alph,string)
    return L[n-1]

def s2n(alph,s):
    l=[]
    slen=len(s)
    i=1
    while (i<=slen):
        l+=rp(alph,s[0:i])
        i+=1
    
    return l.index(s)+1

lets = string.ascii_letters
alph1=random.choice(lets)+random.choice(lets)+random.choice(lets)
alph2=random.choice(lets)+random.choice(lets)+random.choice(lets)
alph3=random.choice(lets)+random.choice(lets)+random.choice(lets)
s1=''
s2=''
s3=''
s4=''
s5=''
for i in range(12):
    s1+=alph1[random.randint(0,2)]
    s2+=alph1[random.randint(0,2)]
    s3+=alph1[random.randint(0,2)]
for i in range(12):
    s4+=alph2[random.randint(0,2)]
for i in range(12):
    s5+=alph3[random.randint(0,2)]

num1=s2n(alph1,s1)
print("Alphabet:",alph1,"string:",s1)
print("Position:",num1,"Result:",n2s(alph1,num1))
print()
num2=s2n(alph1,s2)
print("Alphabet:",alph1,"string:",s2)
print("Position:",num2,"Result:",n2s(alph1,num2))
print()
num3=s2n(alph1,s3)
print("Alphabet:",alph1,"string:",s3)
print("Position:",num3,"Result:",n2s(alph1,num3))
print()
num4=s2n(alph2,s4)
print("Alphabet:",alph2,"string:",s4)
print("Position:",num4,"Result:",n2s(alph2,num4))
print()
num5=s2n(alph3,s5)
print("Alphabet:",alph3,"string:",s5)
print("Position:",num5,"Result:",n2s(alph3,num5))

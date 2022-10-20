#1.
n= int(input('Enter number of lines:'))
def number_pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=' ')
        print(" ")
number_pattern(n)
#2.
n=int(input("Enter number of patterns to be printed:"))
def zero_star_pattern(n):
    print("*")
    for i in range(n):
        for i in range(2,10):
            if i<=5:
                for j in range(1,i+1):
                    if i%2==0:
                        print(0,end='')
                    else:
                        print("*",end='')
                print(" ")
            else:
                for j in range(10-i,0,-1):
                    if i%2==0:
                        print(0,end='')
                    else:
                        print("*",end='')
                print(" ")
                
zero_star_pattern(n)               
 #3. 
def trignometric_pattern(x,n):
    for i in range(1,n+1):
        l=math.sin(x)
        m=math.cos(x)
        if math.ceil(l)-l >l-math.floor(l):
            l=math.floor(l)
        else:
            l=math.ceil(l)
        if math.ceil(m)-m >m-math.floor(m):
            m=math.floor(m)
        else:
            m=math.ceil(m)
        k = i*math.pow(l,i)+i*math.pow(m,i)
        k=int(k)
        if k==0:
            print("$")
        for i in range(k):
            print("$",end="")
        print('')
x=float(input("Enter angle in degrees:"))
n=int(input("Enter number of times:"))
trignometric_pattern(x,n)
#4.
def dictionary_lookup(dictionary,keys):
        for i in range(len(keys)):
            try:
                while dictionary[keys[i]]:
                    print (keys[i],":",dictionary[keys[i]])
                    break

            except:
                 print(keys[i],":",dictionary['other'])
dictionary={'ant':2,'dog':12,'duck':20,'hen':11,'other':99}
keys=['ant','cat','duck','hen','lion','zebra']
dictionary_lookup(dictionary,keys) 
#5.
data = [0.00, 0.12, 0.24, 0.36, 0.48, 0.52, 0.65, 0.50, 0.11, 0.09]
def round_off(data):
    def round(n):
        if math.ceil(n)-n > n-math.floor(n):
            n=math.floor(n)
        else:
            n=math.ceil(n)
        return n    
    x=lambda a : map(round,a)
    return (list(x(data)))
print(round_off(data))
#6. 
def perfect_squares(n):
    l=[]
    for i in range(1,n):
        for j in range(1,i+1):
            if j*j==i:
                l.append(i)
    return(l)
n=int(input("Enter limit:"))    
print(perfect_squares(n))   
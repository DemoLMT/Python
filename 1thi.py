"""import math
a,b,c=map(int,input().split())
if a==0:
    if b==0 & c==0:
        print("WOW")
    elif b==0 & c!=0:
        print("NO")
    else:
        x=-c/b
        print (round(x))
else:
    det = b**2-4*a*c
    if det<0 : print("NO")
    elif det ==0 : 
        x=(-b)/2*a
        print(round(x,2))
    else:
        x1=(-b-math.sqrt(det))/2*a
        x2=(-b+math.sqrt(det))/2*a
        print(f'{x1:.2f}',f'{x2:.2f}')"""
"""def kt(n):
    result=n**0.5
    if(result**2==n): 
        print("YES")
    elif(n==0 or n==1):
        print("NO")
    else: 
        print("NO")

n=int(input())
kt(n)"""
"""import math
a,b,c=map(int,input().split())

cv=a+b+c
nua=cv/2
dt=math.sqrt(nua*(nua-a)*(nua-b)*(nua-c))
if (a+b<=c or a+c<=b or b+c<=a):
    print("NO")
else:
    print(cv,f'{dt:.2f}')
    """
a,b = map(int,input().split())
def gcd(a,b):
    if(b==0): return a
    elif(a%b==0): return b
    else:return gcd(b,a%b)
def bc(a,b):
    return int((a * b) / gcd(a, b))
print(bc(a,b))


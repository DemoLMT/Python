'''Bai1:
d,r = map(int,input().split())
print(2*(d+r))
print(f"{d*r:.2f}")
Bai2:
r = float(input())
pi = 3.14
print(f'{2*pi*r:.3f}',f'{pi*r*r:.3f}')
Bai3:
def ucln(a,b):
    if(b==0): return a
    elif(a%b==0): return b
    return ucln((b),(a%b))
a,b = map(int,input().split())
bcnn = a*b/(ucln(a,b))
print(abs(int(bcnn)))'''
#Bai4
import math
n = int(input())
if( n<0): print("NO")
else:
    re = math.sqrt(n)
    if(re**2==n): print("YES")
    else: print("NO")
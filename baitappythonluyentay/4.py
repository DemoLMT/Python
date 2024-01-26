#pt bac nhat: ax+b=0
'''
def kt(a,b):
    if(a==0 and b!=0):
        return "INVALID"
    elif(a==0 and b==0):
        return "FULL"
    else:
        return float(-b/a)
if __name__ == '__main__':
    a,b = map(int,input().split())
    print(kt(a,b))'''
import math
def ptb2(a,b,c):
    if(a==0):
        if(b==0 and c!=0): return "INVALID"
        elif(b==0 and c==0): return "FULL"
        else:
            return float(-b/a)
    else:
        delta = b**2-4*a*c
        if(delta<0): return "INVALID"
        elif(delta ==0): return float(-b/2*a)
        else:
            x1= float((-b+ math.sqrt(delta))/2*a)
            x2= float((-b- math.sqrt(delta))/2*a)
            return "{0},{1}".format(x1,x2)
if __name__ == '__main__':
    a,b,c=map(int,input().split())
    print(ptb2(a,b,c))
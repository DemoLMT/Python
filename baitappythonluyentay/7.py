def kt(n):
    if (n<2): return 'NO'
    elif (n==2 or n==3): return 'YES'
    else:
        for i in range (1, int(n**1/2)+1):
            if(n%i==0): 
                return 'NO'
    return 'YES'
a= int(input())
print(kt(a))
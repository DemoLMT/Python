def kt(n):
    if (n<1 or n>10000):
        print("Nam k nhuan")
    elif(n%4 == 0 and n%100!=0) or (n%400 == 0):
        print("Nam nhuan")
    else: 
        print("Nam k nhuan")
n = int(input())
kt(n)
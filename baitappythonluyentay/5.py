n = int(input())
sum = 0
sum2=0
for i in range(2,n+1):
    sum+=i
    sum2=sum+2*n
    i+=1
print(sum2)
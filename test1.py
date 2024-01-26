'''
import numpy as np
import matplotlib.pyplot as plt
dientich=np.array([3536,1980,2669,2394,2694,800,4224,3450])
danso =np.array([1864000,1181000,1617000,1295000,2100000,900000,3955000,3200000])
slope,intercept = np.polyfit(dientich,danso,1)
def dudoan(tyle):
    return slope*tyle + intercept
dudoandanso = np.array([2200,3200,4200])
for tyle in dudoandanso:
    dudoanmain = dudoan(tyle)
    print(f"Dan so tuong ung voi dien tich {tyle} la : {dudoanmain}")
#Ve do thi
plt.scatter(dientich, danso, color='red', label='Dữ liệu thực tế')
plt.plot(dientich, dudoan(dientich), color='blue', label='Đường hồi quy tuyến tính')
plt.scatter(dudoandanso, dudoandanso, color='green', label='Dự đoán')
plt.xlabel("Diện tích")
plt.ylabel("Dân số")
plt.legend()
plt.show()
'''
def ckn(n,k):
    if(k==0 or k==n) : return 1
    else: 
        return ckn(n-1,k) + ckn(n-1,k-1)
import math
def permutations(n, k):
    return math.factorial(n) // math.factorial(n - k)
print(ckn(5,3))
print(permutations(5, 2))
'''
#Bai1
a,b,c, x = map(int,input().split())
print(a*x**2 +b*x+c)
#Bai2
n = int(input())
c=[]
for i in range(n):
    c.append (int(input()))
for i in c: 
    if int(i**(1/3) + 0.5)**3 == i:
        print('YES')
    else:
        print('NO')
''''''
import math
def kt(n):
    if(n<2): return "no"
    elif(n==2 or n==3): return "yes"
    else:
        for i  in range(2,int(math.sqrt(n))+1):
            if(n%i==0): return "no"
    return "yes"
n = int(input())
print(kt(n))'''
'''
file_path = r'C:\text.txt'
# Mở file để đọc ('r' là chế độ đọc)
with open(file_path, 'r') as file:
    # Đọc toàn bộ nội dung của file
    content = file.read()
# Hiển thị nội dung đọc được
print(content)

file_path = r'C:\text.txt'
with open(file_path, 'a', encoding='utf-8') as file:
    file.write("Kết quả của bạn là: 42\n")'''

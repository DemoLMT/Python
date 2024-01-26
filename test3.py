def dem_so_lan_xuat_hien(str, x):
    if x== str:
        str +=1
    if i.islower():
        str = str.lower()
    return str.count(x)
str = input()
n = int(input())
lst=[]
for i in range(n):
    lst.append(input())
for i in lst:
    print(dem_so_lan_xuat_hien(str, i))
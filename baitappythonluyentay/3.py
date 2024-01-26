#Nhập một số bất kỳ. Hãy đọc giá trị của số nguyên đó nếu nó có giá trị từ 0 đến 9, ngược lại thông báo không đọc được.
n=int(input())
if(n<0 or n>9): print("khong doc duoc!")
else:
    donvi = ["khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"]
    for i in range(0,10):
        if n == i:
            print(donvi[i])
        
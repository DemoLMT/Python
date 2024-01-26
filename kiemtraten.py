"""Xây dựng chương trình thực hiện cho phép người 
dùng nhập vào danh sách họ tên sinh viên của một lớp. 
Hiển thị ra màn hình các sinh viên vừa nhập có 
tên là Phương ra màn hình.
"""
n = int(input())
lst = []
for i in range (n):
    lst.append(input())
print("Cac ban co ten phuong trong lop la")
for i in lst:
    if(i.lower().endswith("phuong") == True):
        print(i)
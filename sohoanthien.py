def tinh_tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_so_hoan_thien(n):
    return n == tinh_tong_uoc_so(n)

def la_so_thinh_vuong(n):
    return tinh_tong_uoc_so(n) > n

# Nhập số từ người dùng
n = int(input("Nhập một số nguyên dương: "))

# Kiểm tra và in kết quả
if la_so_hoan_thien(n):
    print(f"{n} là số hoàn thiện.")
else:
    print(f"{n} không là số hoàn thiện.")

if la_so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng.")
else:
    print(f"{n} không là số thịnh vượng.")
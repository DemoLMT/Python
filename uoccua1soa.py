def tim_so_luong_uoc_duong(a):
    if a == 0:
        return
    count = 0
    for i in range(1, abs(a) + 1):
        if a % i == 0:
            count += 1
    return count
so_nguyen = int(input())
print(tim_so_luong_uoc_duong(so_nguyen))
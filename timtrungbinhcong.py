def tinh_trung_binh_cong_le(arr):
    tong_le = 0
    so_le = 0
    for num in arr:
        if num % 2 != 0:
            tong_le += num
            so_le += 1
    if so_le == 0:
        return 0
    trung_binh_cong = tong_le / so_le
    return round(trung_binh_cong, 4)
n= int(input())
arr = list(map(int, input().split()*n))
print( tinh_trung_binh_cong_le(arr))
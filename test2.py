def so_ngay_trong_thang(m,y):
    if m == 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            return 29  
        else:
            return 28  
    elif m in [4, 6, 9, 11]:
        return 30  
    else:
        return 31
m,y= map(int,input().split())
d = so_ngay_trong_thang(m,y)
if(m < 0 or m>12 or y<0):
    print("INVALID")
else: print(d)
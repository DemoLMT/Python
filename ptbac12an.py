def giai_he_phuong_trinh(a, b, c, d, e, f):
    dd = a * e - d * b
    dx = c * e - f * b
    dy = a * f - d * c
    
    if dd == 0:
        if dx == 0 and dy == 0:
            print("VOSONGHIEM")
        else:
            print("VONGHIEM")
    else:
        x = round(dx / dd, 2)
        y = round(dy / dd, 2)
        print(f"{x} {y}")

a,b,c,d,e,f = map(float,input().split())
giai_he_phuong_trinh(a, b, c, d, e, f)
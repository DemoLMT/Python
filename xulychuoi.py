def phan_loai_chuoi(chuoi):
    # Khởi tạo biến đếm
    in_hoa = in_thuong = chu_so = ky_tu_dac_biet = khoang_trang = nguyen_am = phu_am = 0

    # Danh sách nguyên âm
    nguyen_am_list = "aeiouAEIOU"

    # Kiểm tra từng ký tự trong chuỗi
    for char in chuoi:
        if char.isupper():
            in_hoa += 1
        elif char.islower():
            in_thuong += 1
        elif char.isdigit():
            chu_so += 1
        elif char.isspace():
            khoang_trang += 1
        else:
            ky_tu_dac_biet += 1

        # Kiểm tra nguyên âm và phụ âm
        if char.isalpha():
            if char.upper() in nguyen_am_list:
                nguyen_am += 1
            else:
                phu_am += 1

    # In kết quả
    print(f"Số chữ in hoa: {in_hoa}")
    print(f"Số chữ in thường: {in_thuong}")
    print(f"Số chữ là chữ số: {chu_so}")
    print(f"Số chữ là ký tự đặc biệt: {ky_tu_dac_biet}")
    print(f"Số chữ là khoảng trắng: {khoang_trang}")
    print(f"Số chữ là Nguyên Âm: {nguyen_am}")
    print(f"Số chữ là Phụ âm: {phu_am}")

# Nhập chuỗi từ người dùng
chuoi = input("Nhập vào một chuỗi: ")

# Gọi hàm và in kết quả
phan_loai_chuoi(chuoi)
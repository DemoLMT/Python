"""
Nhập một số n có tối đa 2 chữ số. 
Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm).
"""
def doc_so(n):
    if n < 0 or n > 99:
        return "Số không hợp lệ. Vui lòng nhập số từ 0 đến 99."
    
    # Tạo danh sách chữ số từ 0 đến 19 và từ 20 đến 90
    donvi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if n < 10:
        return donvi[n]
    elif n % 10 == 0:
        return chuc[n // 10]
    else:
        return chuc[n // 10] + " " + donvi[n % 10]

# Nhập số từ người dùng
n = int(input("Nhập một số (tối đa 2 chữ số): "))

# Gọi hàm và in kết quả
ket_qua = doc_so(n)
print(f"{n} được đọc là: {ket_qua}")
import re

def is_valid_credit_card(card_number):
    # Kiểm tra số thẻ có bắt đầu bằng 4, 5 hoặc 6 và có đúng 16 chữ số không
    if re.match(r"^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$", card_number):
        # Loại bỏ các dấu gạch ngang và kiểm tra xem số còn lại có chứa hơn 1 số lặp liên tiếp không
        cleaned_number = re.sub(r"-", "", card_number)
        if re.search(r"(\d)(\1{3,})", cleaned_number) is None:
            return "Valid"
    return "Invalid"

# Đọc số lượng số thẻ tín dụng từ đầu vào
N = int(input())

# Đọc N số thẻ tín dụng và kiểm tra tính hợp lệ của chúng
for _ in range(N):
    card_number = input().strip()
    print(is_valid_credit_card(card_number))
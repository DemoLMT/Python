import re

# Đọc số lượng dòng văn bản từ đầu vào
N = int(input())

# Đọc N dòng của văn bản
text_lines = [input().strip() for _ in range(N)]

# Hàm thay thế cho re.sub
def replace_and_or(match):
    if match.group(0) == "&&":
        return "and"
    elif match.group(0) == "||":
        return "or"

# Thực hiện thay thế chuỗi "&&" và "||" chỉ khi có khoảng trắng xung quanh
modified_lines = [re.sub(r"(?<= )&&(?= )|(?<= )\|\|(?= )", replace_and_or, line) for line in text_lines]

# Hiển thị kết quả
for line in modified_lines:
    print(line)
def is_vowel(letter):
    return letter in 'aeiouy'

def score_words(words):
    score = 0
    for word in words:
        vowel_count = sum(1 for letter in word if is_vowel(letter))
        if vowel_count % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# Đọc số lượng từ từ đầu vào
n = int(input())

# Đọc danh sách từ từ đầu vào và chuyển thành danh sách
words = input().split()

# Tính điểm số và hiển thị kết quả
print(score_words(words))

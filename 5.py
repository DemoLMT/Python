# Dữ liệu diện tích và dân số của các tỉnh
diện_tích = [1995, 2000, 2005, 2010]
dân_số = [71.9, 77.6, 83.1, 86.9]
# Hàm tính hệ số hồi quy tuyến tính
def linear_regression(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x_squared = sum([x[i] ** 2 for i in range(n)])
    # Tính hệ số hồi quy tuyến tính
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    return m, b
# Hệ số hồi quy tuyến tính
slope, intercept = linear_regression(diện_tích, dân_số)
# Hàm dự đoán dân số dựa trên diện tích
def predict_population(area):
    return slope * area + intercept
# Diện tích của các tỉnh cần dự đoán dân số
diện_tích_dự_đoán = [2014]
# Dự đoán dân số cho các diện tích đã cho
for area in diện_tích_dự_đoán:
    population_predicted = predict_population(area)
    print(f"Dự đoán dân số với diện tích {area} km là: {population_predicted:.2f} người")
# Dữ liệu đầu vào
diện_tích = [3536, 1980, 2669, 2394,2694,800,4224,3450]  # Diện tích các tỉnh (đơn vị: km)
dân_số = [1864000, 1181000, 1617000, 1295000,2100000,900000,3955000,3200000] # Dân số tương ứng với diện tích trên (đơn vị: người)

# Hàm tính hệ số hồi quy tuyến tính bằng phương pháp bình phương tối thiểu
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

# Dự đoán dân số các tỉnh có diện tích 2200, 3200, 4200
def predict_population(area):
    return slope * area + intercept

diện_tích_dự_đoán = [2200, 3200, 4200]
for area in diện_tích_dự_đoán:
    population_predicted = predict_population(area)
    print(f"Dự đoán dân số với diện tích {area} km là: {population_predicted} người")

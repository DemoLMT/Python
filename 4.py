from scipy.stats import linregress
# Dữ liệu diện tích và dân số của các tỉnh
diện_tích = [1995, 2000, 2005, 2010]
dân_số = [71.9, 77.6, 83.1, 86.9]
# Hàm dự đoán dân số dựa trên diện tích
dudoan = lambda area: linregress(diện_tích, dân_số)[0] * area + linregress(diện_tích, dân_số)[1]
# Diện tích của các tỉnh cần dự đoán dân số
diện_tích_dự_đoán = [2014]
# Dự đoán dân số cho các diện tích đã cho
for area in diện_tích_dự_đoán:
    dudoandientich = dudoan(area)
    print(f"Dự đoán dân số với diện tích {area} km là: {dudoandientich:.2f} người")
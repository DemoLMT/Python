import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = [[3536, 1864000], [1980, 1181000], [2669, 1617000], [2394, 1295000], [2694, 2100000],
        [800, 900000], [4224, 3955000], [3450, 3200000]]
area, price = zip(*data)
area, price = [[x] for x in area], [y for y in price]
regr = LinearRegression().fit(area, price)
plt.scatter(*zip(*data), color='red', label='Dữ liệu thực tế')
plt.plot(area, regr.predict(area), color='blue', label='Đường hồi quy tuyến tính')
plt.xlabel("Diện tích")
plt.ylabel("Giá")
plt.legend()
for item, prediction in zip([2200, 3200, 4200], regr.predict([[x] for x in [2200, 3200, 4200]])):
    print(f"Dự đoán diện tích: {item} m2 có giá: {prediction}")
plt.show()
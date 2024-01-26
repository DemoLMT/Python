'''# Dữ liệu đầu vào

Bai 2:'''
#du doan toi pham:
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
# Danh sách các năm
X = np.array([[1995,2000,2005,2010]]).T
# Số lượng tội phạm tương ứng với mỗi năm
y = np.array([[71.9,77.6,83.1,86.9]]).T
# Visualize data 
plt.plot(X, y, 'ro')
plt.axis([1993, 2012,68, 91])
plt.xlabel('Năm (Year)')
plt.ylabel('Số lượng tội phạm (member))')
plt.show()

# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

# Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
print('w = ', w)
# Preparing the fitting line 
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(1994, 2012, 2)
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X.T, y.T, 'ro')     # data 
plt.plot(x0, y0)               # the fitting line
plt.axis([1993, 2012,68, 91])
plt.xlabel('Năm (Year)')
plt.ylabel('Số lượng tội phạm (member))')
plt.show()

y1 = w_1*2014 + w_0
#y2 = w_1*160 + w_0

print( u'Dự đoán số lượng tội phạm năm 2014: %.2f (member), real number: 90.5 (member)'  %(y1) )
#print( u'Predict weight of person with height 160 cm: %.2f (kg), real number: 56 (kg)'  %(y2) )
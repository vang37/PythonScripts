import numpy as np

np.random.seed(0)  # seed for reproducibility


# summa = np.zeros((5,5))
# x1 = np.random.randint(10, size=(7,7))
# w1 = np.random.randint(10, size=(3,3))

# print("x1: ", x1, "w1: ", w1) 

x = np.random.randint(10, size=(3,3))
x1 = np.random.randint(10, size=(3,3,4,8))

w = x1[:,:,:,0]


print(w[0])

# np.random.seed(1)
# A_prev = np.random.randn(10,5,7,4)
# W = np.random.randn(3,3,4,8)
# # summa = np.multiply(x1, w1)

# print("A_prev = np.random.randn(10,5,7,4)")       
# print(A_prev)

# print("W = np.random.randn(3,3,4,1)")       
# print(W)

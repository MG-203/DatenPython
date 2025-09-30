import numpy as np

u = np.array([1,2,3])
v = 10*u
#print(v)

a = np.array([4,5,6])   
#print(a@u)

A = np.array([[2, 0, 0],
[0, 1, 0],
[0, 0, 1]])
#print(A @ a)

B = np.array([[5, 0, 0],
[0, 1, 0],
[0, 0, 1]])
#print(A @ B)


a1 = np.array([20,55,6.5])
a2 = np.array([27.5,3,8])
A1 = np.array([[5,7,9],
               [10,2,0],
               [1,0,1]])
A2 = np.array([[7.5,9,33],
               [0,4,5],
               [2,0,6]])
# print(a1+a2)
# print(a1@a2)
# print(A1+A2)
# print(A1@A2)
# print(A1@a2)

# randnum = np.random.rand()
# print(randnum)
randnums = np.random.rand(10)
# print(randnums)

def random_number_array(x):
    c = []
    for i in x:
        if i >= 0.5:
            c = np.append(c, i)

    return c

print(random_number_array(randnums))
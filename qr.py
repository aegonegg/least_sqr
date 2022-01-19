import numpy as np
from scipy.linalg import qr

from numpy import array
from numpy.linalg import inv
from numpy.linalg import qr
from matplotlib import pyplot

data = array([
[0.05, 0.12],
[0.18, 0.22],
[0.31, 0.35],
[0.42, 0.38],
[0.5, 0.49],
])
from collect import Y1, b1, tpredict

Y=np.array(Y1[0])
b=np.array(b1[0])
X=np.linalg.solve(b, Y)
print(X)
# QR decomposition
Q, R = qr(X)
b = inv(R).dot(Q.T).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)

# plot data and predictions
def plot(x,y):
    pyplot.scatter(X, y)
    pyplot.plot(X, yhat, color='red')
    pyplot.show()

def QR_Decomposition(A):
    n, m = A.shape # get the shape of A
    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u
    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])
    for i in range(1, n):
        u[:, i] = A[:, i]
        for j in range(i):
            u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j] # get each u vector
        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor
    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = A[:, j] @ Q[:, i]
    return Q, R
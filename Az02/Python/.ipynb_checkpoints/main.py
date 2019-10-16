import numpy as np


class perceptron():
    def __init__(self, att):
        self.W = np.zeros((1, att + 1))

    def mul(self, z):
        size = z.shape[0]
        z = z.reshape((size, 1))
        concat = np.zeros((size + 1, 1))
        concat[: size, :] = z[:]
        concat[size:, :] = 1
        return np.sign(np.dot(self.W, concat))[0][0]

    def update(self, alpha, z, y):
        size = z.shape[0]
        z = z.reshape((size, 1))
        concat = np.zeros((size + 1, 1))
        concat[: size, :] = z[:]
        concat[size:, :] = 1
        self.W = self.W - alpha * (self.mul(z) - y) * concat

    def learn(self, x, y, alpha, epoch):
        m = x.shape[1]
        for j in range(epoch):
            for i in range(m):
                self.update(alpha, (x.T[i]), y[i])
                print(self.W)

    def predict(self, x):
        m = x.shape[1]
        result = []
        for i in range(m):
            result.append(self.mul(x.T[i].T))
        return result


# x = np.random.rand(2,10) * 10
# y = np.random.randint(2, size = 10) * 2 - 1
x = np.array([[1,1,1,-1,-4],[1, 2, 4, -2, -5]])
y = np.array([1, 1, 1, -1, -1])
print(x)
print(y)


P = perceptron(2)
P.learn(x, y, 0.2,10)
P.predict(x)
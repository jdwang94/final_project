import numpy as np
import matplotlib.pyplot as plt

"""
Scatterplot & SLR code adapted from: https://www.easymachinelearning.net/introml/implementing-slr-with-python/
"""

class regression():
    def __init__(self,X,Y,name_X,name_Y):
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.name_X = name_X
        self.name_Y = name_Y

    def plot(self):
        plt.scatter(self.X, self.Y)
        plt.xlabel(self.name_X)
        plt.ylabel(self.name_Y)
        plt.grid(True)
        plt.show()

    def SLR(self):
        # Caluclate the slope m and intercept b
        denominator = np.dot(self.X, self.X) - self.X.mean() * self.X.sum()
        m = (np.dot(self.X, self.Y) - self.Y.mean() * self.X.sum()) / denominator
        b = (self.Y.mean() * np.dot(self.X, self.X) - self.X.mean() * np.dot(self.X, self.Y)) / denominator

        # Model
        yHat = m * self.X + b
        print("Y",'=',m,'* X +',b)

if __name__ == "__main__":

    X = [1,2,3,4,5,6]
    Y = [2,4,6,8,10,12]
    test = regression(X,Y,"testX","testY")
    test.plot()
    test.SLR()




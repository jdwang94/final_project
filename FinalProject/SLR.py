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


    def SLR_withoutplot(self):
        # Caluclate the slope m and intercept b
        denominator = np.dot(self.X, self.X) - self.X.mean() * self.X.sum()
        m = (np.dot(self.X, self.Y) - self.Y.mean() * self.X.sum()) / denominator
        b = (self.Y.mean() * np.dot(self.X, self.X) - self.X.mean() * np.dot(self.X, self.Y)) / denominator
        yHat = m * self.X + b
        r_square = self.r_square(yHat)

        # Printing Model
        equation = "Y = " + str(m) + ' * X + ' + str(b)
        #print(equation, r_square)

        return r_square, equation

    def SLR(self):
        # Caluclate the slope m and intercept b
        denominator = np.dot(self.X, self.X) - self.X.mean() * self.X.sum()
        m = (np.dot(self.X, self.Y) - self.Y.mean() * self.X.sum()) / denominator
        b = (self.Y.mean() * np.dot(self.X, self.X) - self.X.mean() * np.dot(self.X, self.Y)) / denominator
        yHat = m * self.X + b
        r_square = self.r_square(yHat)
        N = len(self.X)

        #Plot
        plt.scatter(self.X, self.Y)
        plt.plot(self.X, yHat)
        plt.xlabel(self.name_X)
        plt.ylabel(self.name_Y)
        plt.title("Line of best fit with R-Sqr = " + str(r_square) +" N = " + str(N))
        plt.grid(True)
        plt.show()

        #Printing Model
        equation = "Y = " + str(m) + ' * X + ' + str(b)
        print(equation,r_square)

        return r_square,equation


    def r_square(self,yHat):
       # Evaluating the model using R-Squared
        SSresidual = self.Y - yHat
        SStotal = self.Y - self.Y.mean()

        rSqr = 1 - np.dot(SSresidual, SSresidual) / np.dot(SStotal, SStotal)

        return rSqr

if __name__ == "__main__":

    X = [1,2,3,4,5,6]
    Y = [2,4,6,8,10,12]
    test = regression(X,Y,"testX","testY")
    test.SLR()




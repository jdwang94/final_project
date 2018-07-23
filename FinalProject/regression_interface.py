from SLR import regression
from print_list import print_list

class regression_analysis(print_list):
    def __init__(self,population_object):
        self.population = (population_object)

    def plot_SLR(self):
        # Todo 1. Deal with user input exceptions.
        self.print_options(self.population.columns[1:])
        indep = int(input("Select X (Independent) Variable:"))
        dep = int(input("Select Y (Dependent) Variable:"))
        X = [i[indep] for i in self.population.data]
        print("x", X)
        Y = [i[dep] for i in self.population.data]
        print("y", Y)
        analysis = regression(X, Y, self.population.columns[indep], self.population.columns[dep])
        analysis.SLR()

    def generate_correlation_list(self):
        fh = open('correlations.csv', "w")
        correlation_data = []

        for i in range(1,len(self.population.data[0])-1):
            for j in range(1,len(self.population.data[0])-1):
                if i != j:
                    X = [k[i] for k in self.population.data]
                    print(X)
                    Y = [l[j] for l in self.population.data]
                    print(Y)
                    analysis = regression(X, Y, self.population.columns[i], self.population.columns[j])
                    r_square , equation = analysis.SLR_withoutplot()
                    r = r_square**0.5
                    correlation_data.append([str(r),str(self.population.columns[i]),str(self.population.columns[j]),str(equation)])

        correlation_data.sort(reverse=True)
        for i in range(len(correlation_data)):
            for j in range(len(correlation_data[i])):
                if j != len(correlation_data[i])-1:
                    fh.write(str(correlation_data[i][j]))
                    fh.write(",")
                else:
                    fh.write(str(correlation_data[i][j]))
                    fh.write("\n")
        fh.close()



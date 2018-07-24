from SLR import regression
from print_list import print_list

class InputError(Exception):
    pass

class regression_analysis(print_list):
    def __init__(self,population_object):
        self.population = (population_object)

    def plot_SLR(self):
        """
        Runs function "process_plot_SLR". Exception deals with invalid user inputs.
        """

        try:
            self.process_plot_SLR()
        except InputError as ex:
            print(ex)
            self.plot_SLR()

    def process_plot_SLR(self):

        """
        Prints file_import options for the user
        """
        self.print_options(self.population.columns[1:])

        """
        Asks for user to input independent variable (X) & dependent variable (Y)
        """
        indep = (input("Select X (Independent) Variable:"))
        dep = (input("Select Y (Dependent) Variable:"))

        try:
            indep = int(indep)
            dep = int(dep)
        except:
            raise InputError("\nPlease input a valid integer")


        """
        Data preparation: Removing any "0" values from the dataset
        """
        X = []
        Y = []
        if ( 0 < indep <= len(self.population.columns) ) and ( 0 < dep <= len(self.population.columns) ):

            for i in self.population.data:
                if (i[indep] != 0) and (i[dep] != 0):
                    X.append(i[indep])
                    Y.append(i[dep])
            print("X:", X)
            print("Y:", Y)

            """
            Code to run the regression, from "SLR.py"
            """

            analysis = regression(X, Y, self.population.columns[indep], self.population.columns[dep])
            analysis.SLR()

        else:
            raise InputError("\nPlease input a valid option")

    def generate_correlation_list(self):
        fh = open('correlations.csv', "w")
        correlation_data = []


        for i in range(1,len(self.population.data[0])):
            for j in range(1,len(self.population.data[0])):
                X = []
                Y = []
                if i != j:
                    for line in self.population.data:
                            if (line[i] != 0) and (line[j] != 0):
                                X.append(line[i])
                                Y.append(line[j])
                    print((X))
                    print((Y))
                    analysis = regression(X, Y, self.population.columns[i], self.population.columns[j])
                    r_square , equation = analysis.SLR_withoutplot()
                    r = r_square**0.5
                    correlation_data.append([str(r),str(self.population.columns[i]),str(self.population.columns[j]),str(equation)])

        correlation_data.sort(reverse=True)
        columns_title = ["r-value","Independent Value (X)","Dependent Value (Y)","Equation"]
        for i in range(len(columns_title)):
            if i != len(columns_title)-1:
                fh.write(columns_title[i])
                fh.write(",")
            else:
                fh.write(columns_title[i])
                fh.write("\n")

        for i in range(len(correlation_data)):
            for j in range(len(correlation_data[i])):
                if j != len(correlation_data[i])-1:
                    fh.write(str(correlation_data[i][j]))
                    fh.write(",")
                else:
                    fh.write(str(correlation_data[i][j]))
                    fh.write("\n")
        fh.close()



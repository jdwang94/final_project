class csv():
    def __init__(self,filename):
        """
        Initalize.
        """
        self.fh = open(filename, 'r')
        self.columns = []
        self.data = []

    def extract_data(self):
        """
        Extracts the columns title into "self.columns" & the dataset into "self.data"
        """
        self.columns = self.fh.readline().strip().split(",")
        for line in self.fh:
            items = line.strip().split(',')
            self.data.append(items)

        """
        Data cleaning: Sets any missing data to 0
        """
        no_of_lines = len(self.columns)
        for i in self.data:
            self.data_cleaning(i,no_of_lines)

        """
        Changes all numerical values to a float type. 
        If the value is empty or some form of filler (eg. '...' & ' - '). Sets value to 0
        """
        for i in range(len(self.data)):
            for j in range(1,len(self.data[i])):
                temp = self.data[i][j]
                try:
                    temp = float(temp)
                    self.data[i][j] = temp
                except:
                    self.data[i][j] = 0

    def data_cleaning(self,i,no_of_lines):
        """
        Data cleaning: Sets any missing data to 0. 'i' refers to an entire row of country
        """

        if len(i) == no_of_lines:
            pass
        elif len(i) < no_of_lines:
                for j in range(no_of_lines - len(i)):
                    i.append(0)


    def print_columns(self):
        """
        Prints the column number and column name
        """
        for i in range(len(self.columns)):
            print("{0:02d}:".format(i),self.columns[i])

    def print_data(self):
        """
        rints dataset. Not as useful, since we have __str__
        """
        for i in range(len(self.data)):
            print("{0:10s}".format(self.data[i][0][0:10]), end=" ")
            for j in range(1,len(self.data[0])):
                print("{0:2f}".format(self.data[i][j]), end=" ")
            print("\n")

    def close_file(self):
        """
        Closes file
        """
        self.fh.close()

    def __str__(self):
        """
        Prints datafile in a tabular matrix.
        """
        text = ''
        for i in self.columns:
            text += "{0:10s}".format(i[0:10]) + ' '
        text += '\n'
        for i in range(len(self.data)):
            text += "{0:10s}".format(self.data[i][0][0:10]) + ' '
            for j in range(1,len(self.data[0])):
                text += "{0:10.2f}".format(self.data[i][j]) + ' '
            text += '\n'

        return text




""" For debugging """
if __name__ == '__main__':
    k = csv("2015_genderinequality_csv_cleaned.csv")
    k.extract_data()
    print(k)
    k.close_file()

"""Ideas:
1. We will ask a series of questions, for example:
"On a scale of 1 - 10, how impt do you think labour force participation rate matters for geneder equality?"
We will use this numbers to do some computation, using existing data.

Then we could come out with our own ranking of gender equality

"""
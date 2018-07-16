import logging

class csv():
    def __init__(self):
        """
        Arg:
        'filename' string: string name of the file to be read
        """
        self.columns = []
        self.data = []
        logging.basicConfig(filename="log.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

    def extract_data(self,filename):
        fh = open(filename, 'r')
        logging.debug('Attempting to extract %s' %filename)

        """
        Extracts the columns title into "self.columns" & the dataset into "self.data"
        """
        self.columns = fh.readline().strip().split(",")
        for line in fh:
            items = line.strip().split(',')
            self.data.append(items)

        """
        1st Data cleaning: Any missing data is set to the default value of 0
        """
        no_of_variables = len(self.columns)
        for i in self.data:
            self.data_cleaning(i,no_of_variables)

        """
        2nd Data cleaning:
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

        """
        Debugging Line:
        """
        logging.debug("Extracted %s" %filename)

        """
        Close File
        """
        fh.close()
    def data_cleaning(self,i,no_of_variables):
        """
        Data cleaning: For data sets that have missing values/incomplete, appends a default value of '0'.

        Arg:
        'i' list: Row of data that is to be cleaned
        'no_of_lines' integer: No. of variables that are supposed to be in the data set.

        Returns:
        Cleaned row of data, where there are no missing values.
        """

        if len(i) == no_of_variables:
            pass
        elif len(i) < no_of_variables:
                for j in range(no_of_variables - len(i)):
                    i.append(0)
                    """
                    Debugging Line: To show that data cleaning has been performed, and on which line
                    """
                logging.debug("%s row has been cleaned." %i)


    def print_columns(self):
        """
        Prints the column number and column name
        """
        for i in range(len(self.columns)):
            print("{0:02d}:".format(i),self.columns[i])

    def print_data(self):
        """
        Prints dataset. Not as useful, since we have __str__
        """
        for i in range(len(self.data)):
            print("{0:10s}".format(self.data[i][0][0:10]), end=" ")
            for j in range(1,len(self.data[0])):
                print("{0:2f}".format(self.data[i][j]), end=" ")
            print("\n")


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
    k = csv()
    k.extract_data("2015_genderinequality_csv_cleaned.csv")
    print(k)

from read_csv import csv
import logging

class population(csv):
    def __init__(self):
        csv.__init__(self)

        """
        self._list_of_countries is set as a protected variable (encapsulation). 
        The main use of this list is to check if a country is already in the population.
        If the country is in the population, the program would append the data to the existing country
        Else, it would create a new row of data.
        This is to prevent any tampering/printing function in the "user_interface" module.
        """

        self._list_of_countries = []


    def import_csv(self,filename):
        """
        Imports "filename" (a csv file) into the existing population. Does an index based on the first column of the data
        Empty values will be set to '0'.

        Arg:
        'filename' string: string name of the file to be read
        """
        data_object = csv()  #Deal with exceptions
        data_object.extract_data(filename)

        before_column = len(self.columns)
        for i in range(1,len(data_object.columns)): #For Column Index
            self.columns.append(data_object.columns[i])

        """
        If the population is empty, simply add the csv file into the population.
        """
        if len(self.data) == 0:
            self.data = data_object.data
            self.list_of_countries = [data_object.data[i][0] for i in range(len(data_object.data))]
            self.columns.insert(0,data_object.columns[0])
            logging.debug('Population is empty. Added (%s) into the population object' %filename)

        else:
            """
            If the population is not empty, indexes the country's data values and adds it into the existing population
            """
            for i in range(len(data_object.data)):
                if data_object.data[i][0] in self.list_of_countries:
                    index_number = self.list_of_countries.index(data_object.data[i][0])
                    for j in range(1,len(data_object.data[i])):
                        self.data[index_number].append(data_object.data[i][j])
                else:
                    """
                    If there is a new country, not found in the existing population, add this country into the population
                    """
                    self.list_of_countries.append(data_object.data[i][0])
                    self.data.append([data_object.data[i][0]])
                    for j in range(1,before_column):
                        self.data[-1].append(0)
                    for k in range(1,len(data_object.data[i])):
                        self.data[-1].append(data_object.data[i][k])
                    logging.debug('New country (%s) found.' %data_object.data[i][0])

            """
            Data cleaning: Any missing data is set to the default value of 0
            """
            for i in self.data:
                no_of_lines = len(self.columns)
                csv.data_cleaning(self,i,no_of_lines)

        logging.debug('Added (%s) into the population object' %filename)

""" For debugging """
if __name__ == '__main__':
    all_csv = population()
    all_csv.import_csv("2015_genderinequality_csv_cleaned.csv")
    all_csv.import_csv("2015_HDI_csv_cleaned.csv")
    print(all_csv)
    for i in range(len(all_csv.columns)):
        print(i+1,all_csv.columns[i])
    print(len(all_csv.list_of_countries))




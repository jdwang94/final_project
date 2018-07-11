from read_csv import csv

class population(csv):
    def __init__(self):
        self.columns = []
        self.data = []
        self.list_of_countries = []

    def import_csv(self,filename):
        """Imports "filename" (a csv file) into the existing population.
        Does an index based on the first column of the data
        Empty values will be set to '0' for convinience.  """
        data_object = csv(filename)  #Deal with exceptions
        data_object.extract_data()

        before_column = len(self.columns)
        for i in data_object.columns: #For Column Index
            self.columns.append(i)

        """If the population is empty, simply add the csv file into the population."""
        if len(self.data) == 0:
            self.data = data_object.data
            self.list_of_countries = [data_object.data[i][0] for i in range(len(data_object.data))]

        else:
            """If the population is not empty, properly indexes the country's data values and adds it into the existing population"""
            for i in range(len(data_object.data)):
                if data_object.data[i][0] in self.list_of_countries:
                    index_number = self.list_of_countries.index(data_object.data[i][0])
                    for j in range(1,len(data_object.data[i])):
                        self.data[index_number].append(data_object.data[i][j])
                else:
                    """If there is a new country, not found in the existing population, add this country into the population"""
                    self.list_of_countries.append(data_object.data[i][0])
                    self.data.append([data_object.data[i][0]])
                    for j in range(1,before_column):
                        self.data[-1].append(0)
                    for k in range(1,len(data_object.data[i])):
                        self.data[-1].append(data_object.data[i][k])

            """Data cleaning"""
            for i in self.data:
                no_of_lines = len(self.columns)
                csv.data_cleaning(self,i,no_of_lines)


""" For debugging """
if __name__ == '__main__':
    all_csv = population()
    all_csv.import_csv("2015_HDI_csv_cleaned.csv")
    all_csv.print_data()
    all_csv.import_csv("2015_genderinequality_csv_cleaned.csv")
    all_csv.print_data()


    #for i in range(len(all_csv.list_of_countries)):
        #print(all_csv.list_of_countries[i])



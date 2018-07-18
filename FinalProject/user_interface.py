from population import population
import os
import _csv as debugcsv #TO BE DELETED ONCE DEBUGGINS IS DONE
import shelve
import logging

class InputError(Exception):
    pass

"""
Potential additions:
1. Clear data function
"""

class user_interface():

    def __init__(self):
        self.menu = ["Select files for import","View Data","Correlation analysis","Shelve Data"]
        self.view_data_options = ['View countries', 'View variables', 'View entire dataset', 'Output dataset as a csv file']
        self.population = population()

    def menu_page(self):
        """
        Runs function "process_menu_page". Exception deals with invalid user inputs.
        """
        try:
            self.process_menu_page()
        except InputError as ex:
            print(ex)
            self.menu_page()

    def process_menu_page(self):
        """
        Prints menu options for the user
        """
        self.print_options(self.menu,1)

        """
        Asks for user input. Then redirects to the appropriate function.
        """
        n = (input("What would you like to do? Please input the correpsonding integer:"))

        if n == str(1):
            self.file_import()
        elif n == str(2):
            self.view_data()
        elif n == str(3):
            self.analysis()
        elif n == str(4):
            self.save()
        elif n == str('q'):
            quit()
        else:
            raise InputError("Please input a valid digit or 'q'")

    def view_data(self):
        """
        Runs function "process_view_page". Exception deals with invalid user inputs.

        If there is no csv file imported into the program, prompts user to import in a csv file before attempting
        to view the imported data.
        """
        if self.population.data != []:
            try:
               self.process_view_data()
            except InputError as ex:
                print(ex)
                self.view_data()

        else:
            print("\nThere is no imported data to view. Please import in some data before trying to view data")
            self.menu_page()

    def process_view_data(self):
        """
        Prints view_data options for the user
        """
        self.print_options(self.view_data_options,2)

        """
         Asks for user input. Then redirects to the appropriate function.
        """
        n = (input("What would you like to view? Please input the correpsonding integer:"))

        if n == str(1):
            self.print_options(self.population.list_of_countries)
            self.process_view_data()
        elif n == str(2):
            self.print_options(self.population.columns)
            self.process_view_data()
        elif n == str(3):
            print(self.population)
            self.process_view_data()
        elif n == str(4):
            self.csv_output()
            file_directory = os.getcwd() + "\output.csv"
            print("File output completed. Saved at %s" %file_directory)
            self.process_view_data()
        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise InputError("Please input a valid digit, 'q' or 'b'")

    def csv_output(self):
        """
        Creates an output csv file, based on all the csv files imported into the system
        """
        fh = open("output.csv",'w')
        for i in range(len(self.population.columns)):
            if i != len(self.population.columns)-1:
                fh.write(str(self.population.columns[i]))
                fh.write(",")
            else:
                fh.write(str(self.population.columns[i]))
                fh.write("\n")

        for i in range(len(self.population.data)):
            for j in range(len(self.population.data[i])):
                if j != len(self.population.data[i])-1:
                    fh.write(str(self.population.data[i][j]))
                    fh.write(",")
                else:
                    fh.write(str(self.population.data[i][j]))
                    fh.write("\n")
        fh.close()

    def file_import(self):
        try:
            self.process_file_import()
        except InputError as ex:
            print(ex)
            self.file_import()

    def process_file_import(self):
        """
        Prints file_import options for the user
        """
        directory_csv = [file for file in os.listdir() if file.endswith(".csv")]
        self.print_options(directory_csv,2)

        """
        Asks for user input. Then imports csv file based on user's input.
        """
        n = (input("Which csv would you like to import? Please input the corresponding integer:"))

        try:
            n = int(n)
        except:
            pass

        if isinstance(n, int) is True and n <= len(directory_csv):
            self.population.import_csv(directory_csv[int(n)-1])

            """Debug"""
            myFile = open('debugging.csv', 'w', newline='')
            with myFile:
                writer = debugcsv.writer(myFile)
                writer.writerows(self.population.data)

            print(self.population)  #Debugging line
            """End of debugging"""
            self.file_import()
        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise InputError("\nPlease input a valid digit, 'q' or 'b'")

    def analysis(self):
        pass

    def save(self):
        try:
            self.process_save()
        except InputError as ex:
            print(ex)
            self.save()

    def process_save(self):
        options = ["Save current dataset","Load previous dataset"]
        self.print_options(options,2)

        n = (input("What would you like to do? Please input the correpsonding integer:"))
        sf = shelve.open("data")
        if str(n) == "1":
            sf['columns'] = self.population.columns
            sf['data'] = self.population.data
            sf['countries'] = self.population.list_of_countries
            print("Data has been saved into a shelve file")
            logging.debug("Current dataset saved")
            self.save()

        elif str(n) == "2":
            self.population.columns = sf['columns']
            self.population.data = sf['data']
            self.population.list_of_countries = sf['countries']
            print("Data has been loaded")
            logging.debug("Dataset loaded from shelve file")
            self.save()

        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise InputError("Please input a valid digit, 'q' or 'b'")

    def print_options(self,list_of_options,k=0):
        """
        Args:
        'list_of_options' List: list of options which is to be displayed to the user.
        'k' Int: Type of menu to be printed

        Returns:
        Prints a formatted menu options onto the user's screen
        """
        print("\n")
        for i in range(len(list_of_options)):
            print(i+1, list_of_options[i])

        if k == 1:
            print("\nType 'q' to quit")
        elif k == 2:
            print("\nType 'q' to quit")
            print("Type 'b' to back")

if __name__ == '__main__':
    test = user_interface()
    test.menu_page()
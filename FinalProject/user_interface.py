from population import population
import os
import shelve
import logging
from regression_interface import regression_analysis
from print_list import print_list

class InputError(Exception):
    pass

class user_interface(print_list):

    def __init__(self):
        self.menu = ["Select files for import","View Data","Simple Linear Regression","Shelve Data"]
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
        """
        Runs function "process_file_import". Exception deals with invalid user inputs.
        """

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
            print(self.population)
            self.file_import()
        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise InputError("\nPlease input a valid digit, 'q' or 'b'")

    def analysis(self):
        """
        Runs function "process_analysis". Exception deals with invalid user inputs.

        If there is no csv file imported into the program, prompts user to import in a csv file before attempting
        to analyse the imported data.
        """
        if self.population.data != []:
            try:
                self.process_analysis()
            except InputError as ex:
                print(ex)
                self.analysis()
        else:
            print("\nThere is no imported data to analyse. Please import in some data before trying to analyse data")
            self.menu_page()

    def process_analysis(self):
        """
        Prints analysis options for the user
        """

        menu_options = ["Simple Linear Regression","Generate correlation list"]
        self.print_options(menu_options,2)

        """
        Asks for user input. Then performs analysis based on user's input.
        """
        n = (input("Which analysis would you like to do? Please input the corresponding integer:"))
        regression_module = regression_analysis(self.population)
        if n == str(1):
            regression_module.plot_SLR()
            self.analysis()
        elif n == str(2):
            regression_module.generate_correlation_list()
            self.analysis()
        elif n == str('q'):
            quit()
        elif n == str('b'):
            self.menu_page()
        else:
            raise InputError("\nPlease input a valid digit, 'q' or 'b'")

    def save(self):
        try:
            self.process_save()
        except InputError as ex:
            print(ex)
            self.save()
        except KeyError:
            print("No saved data to save/load. Please save some data before loading in data.")
            self.menu_page()

    def process_save(self):
        """
        Saves or loads data base on user's input.
        If there is no data in the population object, or no saved file, raise a KeyError
        """
        options = ["Save current dataset","Load previous dataset"]
        self.print_options(options,2)

        n = (input("What would you like to do? Please input the correpsonding integer:"))
        sf = shelve.open("data")

        if str(n) == "1":
            if self.population.data != []:
                sf['columns'] = self.population.columns
                sf['data'] = self.population.data
                sf['countries'] = self.population._list_of_countries
                print("Data has been saved into a shelve file")
                logging.debug("Current dataset saved")
                self.save()
            else:
                raise KeyError

        elif str(n) == "2":
            self.population.columns = sf['columns']
            self.population.data = sf['data']
            self.population._list_of_countries = sf['countries']
            print("Data has been loaded")
            logging.debug("Dataset loaded from shelve file")
            self.save()

        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise InputError("Please input a valid digit, 'q' or 'b'")

        sf.close()


if __name__ == '__main__':
    test = user_interface()
    test.menu_page()
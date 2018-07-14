from population import population
import os
import _csv as debugcsv #TO BE DELETED ONCE DEBUGGINS IS DONE

class error(Exception): pass

class user_interface():

    def __init__(self):
        self.menu = ["Select files for import","View Data","Correlation analysis"]
        self.population = population()

    def menu_page(self):
        """
        Todo: Fix this!!!
        """
        try:
            self.process_menu_page()
        except error:
            print("Please input in a valid digit or 'q'")
            self.menu_page()

    def process_menu_page(self):
        """
        Prints menu options for the user
        """
        self.print_options(self.menu)

        """
        Asks for user input. Then redirects to the appropriate function.
        """
        n = (input("What would you like to do? Please input the correpsonding integer:"))
        while n != 'q':
            if n == str(1):
                self.file_import()
            elif n == str(2):
                self.view_data()
            elif n == str(3):
                self.analysis()
            else:
                raise error


    def view_data2(self): pass
    #todo: If dataset is empty, do not run the command

    def view_data(self):
        """
        Prints view_data options for the user
        """
        view_data_options = ['View countries','View variables','View entire dataset', 'Output dataset as a csv file']
        self.print_options(view_data_options)
        print('Type "b" to back')

        """
         Asks for user input. Then redirects to the appropriate function.
        """
        n = (input("What would you like to view? Please input the correpsonding integer:"))

        if n == str(1):
            self.print_options(self.population.list_of_countries)
        elif n == str(2):
            self.print_options(self.population.columns)
        elif n == str(3):
            print(self.population)
        elif n == str(4):
            self.csv_output()
            print("file output done")
        elif n == 'q':
            quit()
        elif n == 'b':
            self.menu_page()
        else:
            raise Exception

    def csv_output(self):
        """
        Ouputs a new csv file.
        Its contents include all csv files that are extracted by previous functions.
        """
        fh = open("output.csv",'w')
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
        Prints file_import options for the user
        """
        directory_csv=[file for file in os.listdir() if file.endswith(".csv")]
        self.print_options(directory_csv)
        print('Type "b" to back')

        """
        Asks for user input. Then redirects to the appropriate function.
        """
        n = (input("Which csv would you like to import? Please input the corresponding integer:"))
        if n != 'q' and n != 'b' and int(n) <= len(directory_csv):
            self.population.import_csv(directory_csv[int(n)-1])

            """debug"""
            myFile = open('debugging.csv', 'w',newline='')
            with myFile:
                writer = debugcsv.writer(myFile)
                writer.writerows(self.population.data)

            print(self.population)  #Debugging line
            """end of debugging"""

            self.file_import()
        elif n == 'q':
            quit()
        elif n == 'b':
            self.process_menu_page()
        else:
            raise Exception

    def analysis(self):
        pass

    def print_options(self,list_of_options):
        """
        Args:
        'list_of_options' List: list of options which is to be displayed to the user.

        Returns:
        Prints onto user's screen, a formatted Menu Page
        """
        print("\n")
        for i in range(len(list_of_options)):
            print(i+1, list_of_options[i])
        print('\nType "q" to quit')
if __name__ == '__main__':
    test = user_interface()
    test.process_menu_page()
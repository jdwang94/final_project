from population import population
import os
import _csv as debugcsv #TO BE DELETED ONCE DEBUGGINS IS DONE


class user_interface():

    def __init__(self):
        self.menu = ["Select files for import","Correlation analysis"]
        self.population = population()

    def menu_page(self): #Todo exceptions for non-integer input
        for i in range(len(self.menu)):
            print(i+1, self.menu[i])
        print('\nType "q" to quit')

        n = (input("What would you like to do? Please input the correpsonding integer:"))
        while n != 'q':
            if n == str(1):
                self.file_import()
            elif n == str(2):
                self.analysis()
            else:
                raise Exception

    def file_import(self):
        directory_csv=[file for file in os.listdir() if file.endswith(".csv")]
        for i in range(len(directory_csv)):
            print(i+1, directory_csv[i])

        n = (input("Which csv would you like to import? Please input the corresponding integer:"))
        if n != 'q' and int(n) <= len(directory_csv):
            self.population.import_csv(directory_csv[int(n)-1])

            """debug"""
            myFile = open('debugging.csv', 'w')
            with myFile:
                writer = debugcsv.writer(myFile)
                writer.writerows(self.population.data)

            print(self.population)  #Debugging line
            """end of debugging"""
            self.file_import()
        elif n == 'q':
            quit()
        else:
            raise Exception

    def analysis(self):
        pass

if __name__ == '__main__':
    test = user_interface()
    test.menu_page()
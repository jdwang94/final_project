class print_list():
    def __init__(self):
        pass

    def print_options(self, list_of_options, k=0):
        """
        Args:
        'list_of_options' List: list of options which is to be displayed to the user.
        'k' Int: Type of menu to be printed

        Returns:
        Prints a formatted menu options onto the user's screen
        If k == 1, prints out a line that tells user to press 'q' to quit
        If k == 2, prints out 2 lines that tells user to press 'q' to quit or 'b' to back
        """
        print("\n")
        for i in range(len(list_of_options)):
            print(i + 1, list_of_options[i])

        if k == 1:
            print("\nType 'q' to quit")
        elif k == 2:
            print("\nType 'q' to quit")
            print("Type 'b' to back")
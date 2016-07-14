import time

class PrintFunctions():

    def PressAny(self):
        inp = input("Press enter to continue... ")

    #Prints a single line, with 1 through 100, which it appears to append to the end of the line.
    def PrintLineTest(self):
        msg = "Testing "
        for i in range(100):
            msg += " "  + str(i)
            print(msg)
            time.sleep(.5)
            for x in msg:
                print('\b')


    # Print Multiple Lines.
    # Params: List of strings to print. Each takes up one line in the Output
    def PrintMultiLine(self, list):
        for item in list:
            print(item)

    # Implementation 1 - Send a huge number of backspaces to push items off screen.
    # Params: Bumps up the
    def PrintPage(self, message):
        for i in range(100):
            print('\b')
        print(message)

    # Trying to make a method to check for the quit key-combo before sending instructions to next command
    # No luck yet, even though quitState is changed in this method, the while loop in main keeps going.
    def GetInput(self, prompt):
          return str(input(prompt))



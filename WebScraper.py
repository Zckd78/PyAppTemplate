import webbrowser
import PrintFunctions

quit_State = False
quit_String = "back"

class Webscraper():

    def Welcome(self):

        welcomeMessage = "Web Scraper Menu".center(200,'=')
        pf = PrintFunctions.PrintFunctions()
        options_List = ['1 : Web Scraper','2 : File ']
        print("Type Url to open: \n")

        quit_State = False

        # Main running loop
        # Program Flow at the Macro Scale
        while(quit_State != True):
            message = input("URL> ")
            quit_State = self.QuitCheck(message)

            self.Proceed(message)



    def QuitCheck(self,input):
        if(input[0] == "q" and input[1] == "!"):
            global quit_State
            quit_State = True
            return

    def OpenPage(self, url):
        webbrowser.open(url)


    def Proceed(self, url):

        backState = False

        if(len(url) > 0):            
            res = requests.request("www.google.com")
            print(res.raw)

        while(backState != True):
            cmd = input("")
            if(cmd == quit_String):
                quit_State = True



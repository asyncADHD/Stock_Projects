
import yahoo_fin.stock_info as si

# CLI colors 

def strRed(skk):         return "\033[91m {}\033[00m".format(skk)
def strGreen(skk):       return "\033[92m {}\033[00m".format(skk)
def strYellow(skk):      return "\033[93m {}\033[00m".format(skk)
def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def strPurple(skk):      return "\033[95m {}\033[00m".format(skk)
def strCyan(skk):        return "\033[96m {}\033[00m".format(skk)
def strLightGray(skk):   return "\033[97m {}\033[00m".format(skk)
def strBlack(skk):       return "\033[98m {}\033[00m".format(skk)
def strBold(skk):        return "\033[1m {}\033[0m".format(skk)


class CLI():
    def __init__(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "-g": self.get,
            "-oc": self.otpCode,
            "-h": self.history,
            "-n": self.news,
            "-q": self.quote,
            "-c": self.chart,
            "-co": self.company,
            "-o": self.option
        }


    # CLI color defnitions 




    def cli_welcome(self):
        print (strYellow("-" * 47 ))
        print (strPurple("|") + strBold(strCyan("  Welcome to the Stock Price Analyzer CLI  ")) + strPurple("|"))
        print (strPurple("|") + (" " * 5 ) + strGreen("Type 'help' for a list of commands")+ (" " * 5) + strPurple("|"))
        print (strYellow("-" * 47 ))

    def help(self):
        print("-Commands List-")
        print("help - Shows this list of commands")
    
    def exit(self):
        print("Exiting CLI")
        exit()
    
    def get(self, symbol):
        pass
    
    def otpCode(self, symbol):
        pass
    
    def history(self, symbol):
        pass

    def news(self, symbol):
        pass
    
    def quote(self, symbol):
        pass
    
    def chart(self, symbol):
        pass
    
    def company(self, symbol):
        pass
    
    def option(self, symbol):
        pass


if __name__ == "__main__":
    cli = CLI()
    cli.cli_welcome()
    while True:
        command = input("Enter command: ")
        if command == "help":
            cli.help()
        elif command == "exit":
            cli.exit()


    



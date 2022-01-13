import os
import json
import glob
import robin_stocks.robinhood as rs

from urllib.request import urlopen, Request

class Bot:
    # Meta Data
    Bot_List = []
    bot_number = 0

    def __init__(self, username = "", password = "", name = ""):
        # Handling
        if (name == ""):
            name = username

        # Meta info for multiple bots
        Bot.Bot_List.append(self)
        Bot.bot_number += 1
        self.bot_number = Bot.bot_number

        # Data Constructor
        self.username = username
        self.password = password
        self.name = name

        # "Hashing" password for display and identification
        # Yes I'm aware that this is not actually hashing, it is called a play on words because I am using hashtags
        hashed_password = password[0:3]
        for i in range(0, len(self.password)-3):
            hashed_password += "#"
        self.hashed_password = hashed_password

        print("")
        print(" __    __  __            __                __                               ")
        print("/  |  /  |/  |          /  |              /  |                              ")
        print("$$ |  $$ |$$/   ______  $$ |____          $$ |        ______   __   __   __ ")
        print("$$ |__$$ |/  | /      \ $$      \  ______ $$ |       /      \ /  | /  | /  |")
        print("$$    $$ |$$ |/$$$$$$  |$$$$$$$  |/      |$$ |      /$$$$$$  |$$ | $$ | $$ |")
        print("$$$$$$$$ |$$ |$$ |  $$ |$$ |  $$ |$$$$$$/ $$ |      $$ |  $$ |$$ | $$ | $$ |")
        print("$$ |  $$ |$$ |$$ \__$$ |$$ |  $$ |        $$ |_____ $$ \__$$ |$$ \_$$ \_$$ |")
        print("$$ |  $$ |$$ |$$    $$ |$$ |  $$ |        $$       |$$    $$/ $$   $$   $$/ ")
        print("$$/   $$/ $$/  $$$$$$$ |$$/   $$/         $$$$$$$$/  $$$$$$/   $$$$$/$$$$/  ")
        print("              /  \__$$ |                                                    ")
        print("              $$    $$/                                                     ")
        print("               $$$$$$/                                                      ")
        print("")
        print("# Current Bot ==================================================================")
        print("# Bot Number   : " + str(self.bot_number))
        print("# Bot Name     : " + str(self.name) if (name != "") else "Not Defined")
        print("# Bot Username : " + self.username if (username != "") else "Not Defined")
        print("# Bot password : " + self.hashed_password if (hashed_password != "") else "Not Defined")
        print("# ==============================================================================")
        print("# author       : Reed Graff")
        print("# website      : TheReedGraff.com")
        print("# linkedin     : https://www.linkedin.com/in/ReedGraff")
        print("# github       : https://github.com/ReedGraff")
        print("# email        : RangerGraff@gmail.com")
        print("# version      : 1.0")
        print("# ==============================================================================")
        print("")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}

        if (username != "" and password !=  ""):
            rs.login(username, password)

    ### Meta
    def Info(self, unhash = False):
        if unhash:
            password = self.password
        else:
            password = self.hashed_password

        print("")
        print("# Current Bot ==================================================================")
        print("# Bot Number   : " + str(self.bot_number))
        print("# Bot Username : " + self.username)
        print("# Bot password : " + password)
        print("# ==============================================================================")
        print("")

    def Holdings(self):
        my_stocks = rs.build_holdings()
        df = pd.DataFrame(my_stocks)

    def Functions(self, type):
        if type == "Find":
            print("Here are all of the find functions")
        elif type == "Finance":
            print("Here are all of the Finance functions")
        else:
            print("Here are all of the Algorithm functions")

    def Transactions(self):
        print("Here are all of the recent transactions: \n")

        file = open('Assets/Transactions.json')
        data = json.load(file)
        return data

    
    def Login(self, username, password):
        rs.login(username, password)
        self.username = username
        self.password = password

        # Hashed Password
        hashed_password = password[0:3]
        for i in range(0, len(self.password)-3):
            hashed_password += "#"
        self.hashed_password = hashed_password

    def LogOut(self):
        rs.logout()




    ### Primary
    def Find(self, input_data):
        """
        # Example input data
        {
            "function_name": "Some_Random_name",
            "parameters": [
                "Random stock name"
            ]
        }
        """

        # Declare variables for importing
        package = self.Find_Function_Path("Find", input_data["function_name"]).replace("\\", "/").replace(".py", "").replace("/", ".")
        file_name = "_" + input_data["function_name"]
        name = input_data["function_name"]

        # Dynamically import file function & set as attribute of class       
        setattr(Bot, 'imported', getattr(__import__(package, fromlist=[file_name]), name))

        # Dynamically call function
        find_data = self.imported(input_data)

        # Return the new data
        return find_data

    def Finance(self, input_data):
        """
        # Example input data
        {
            "function_name": "Some_Random_name",
            "parameters": [
                "Random stock name"
            ]
        }
        """

        # Declare variables for importing
        package = self.Find_Function_Path("Finance", input_data["function_name"]).replace("\\", "/").replace(".py", "").replace("/", ".")
        file_name = "_" + input_data["function_name"]
        name = input_data["function_name"]

        # Dynamically import file function & set as attribute of class       
        setattr(Bot, 'imported', getattr(__import__(package, fromlist=[file_name]), name))

        # Dynamically call function
        finance_data = self.imported(input_data)

        # Return the new data
        return finance_data

    def Algorithm(self, data):
        return 0




    ### Supporting Functions
    def Find_Function_Path(self, function_type, name):
        file_strux = ["Find", "Finance", "Algorithm"]
        file_num = file_strux.index(function_type) + 1
        path = "Bot/" + str(file_num) + "_" + function_type

        file_path = glob.glob(path + "/**/_" + name + ".py", recursive = True)[0]
        return file_path
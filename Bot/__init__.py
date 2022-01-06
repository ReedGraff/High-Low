import os
import json
import glob
import robin_stocks as rs

from urllib.request import urlopen, Request

class Bot:
    # Meta Data
    Bot_List = []
    bot_number = 0

    def __init__(self, username, password, name = username):
        # Meta info for multiple bots
        Bot.Bot_List.append(self)
        Bot.bot_number += 1
        self.bot_number = Bot.bot_number

        # Data Constructor
        self.username = username
        self.password = password

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
        print("# Bot Name     : " + str(self.name))
        print("# Bot Username : " + self.username
        print("# Bot password : " + self.hashed_password
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

        # Robinhood initialization
        rs.login(username,password)

    ### Meta
    def Info(self, unhash = False):
        if unhash:
            password = self.password
        else:
            password = self.hashed_password

        print("")
        print("# Current Bot ==================================================================")
        print("# Bot Number   : " + str(self.bot_number))
        print("# Bot Username : " + self.username
        print("# Bot password : " + password
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
        print("Here are all of the recent transactions")



    ### Primary
    def Find(self, data):
        """
        # Example input data
        {
            "function_name": "Some_Random_name",
            "parameters": [
                "Random stock name"
            ]
        }
        """
        # Dynamically Import Find function
        from .Find._FindV1 import FindV1

        # Return Find data


        """
        # Example Find Data
        {
            "Ticker": "TSLA",
            ""
        }
        """

        return data

    def Finance(self, data):
        return 0

    def Algorithm(self, data):
        return 0


    ###
    def Find_Function(self, function_type, name):
        file_strux = ["Find", "Finance", "Algorithm"]
        file_num = file_strux.indexOf(function_type) + 1
        path = "./" + file_num + "_" + function_type

        text_files = glob.glob(path + "/**/" + name + ".py", recursive = True)
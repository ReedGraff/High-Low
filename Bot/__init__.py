import json
from urllib.request import urlopen, Request

class Bot:
    # Import Find
    from .Find._FindV1 import FindV1

    # Import Execute
    from .Execute._Buy import Buy
    from .Execute._Sell import Sell

    # Meta Data
    Bot_List = []
    bot_number = 0

    def __init__(self, chain, protocols = []):

        Bot.Bot_List.append(self)
        Bot.bot_number += 1
        self.bot_number = Bot.bot_number

        print("")
        print(" ________  ________      ___    ___ ________  __________ ________          ________  ________  _________   ")
        print("|\   ____\|\   __  \    |\  \  /  /|\   __  \|\___   ___\\\   __  \        |\   __  \|\   __  \|\___   ___\ ")
        print("\ \  \___|\ \  \/\  \   \ \  \/  / | \  \|\  \|___ \  \_\ \  \\\\\  \       \ \  \|\  \ \  \\\\\  \|___\  \__| ")
        print(" \ \  \    \ \   _  _\   \ \    / / \ \   ____\   \ \  \ \ \  \\\\\  \       \ \   __  \ \  \\\\\  \  \ \  \  ")
        print("  \ \  \____\ \  \\\  \    \/   / /   \ \  \___|    \ \  \ \ \  \\\\\  \       \ \  \|\  \ \  \\\\\  \  \ \  \ ")
        print("   \ \_______\ \__\\\ _\ __/   / /     \ \__\        \ \__\ \ \_______\       \ \_______\ \_______\  \ \__\\")
        print("    \|_______|\|__|\|__|\____/ /       \|__|         \|__|  \|_______|        \|_______|\|_______|   \|__|")
        print("                       \|____|/                                                                             ")
        print("")
        print("# Current Bot ==================================================================")
        print("# Bot Number   : " + str(self.bot_number))
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

        # Chain / Network
        accepted_chains = ["Ethereum Mainnet", "Binance Smart Chain Mainnet", "Polygon Mainnet", "Optimistic Ethereum", "Arbitrum One"]
        
        if chain not in accepted_chains:
            out = """
\n\n# ==============================================================================
# The entered chain/network is currently not accepted by the 1Inch API
# Below are the currently accepted chains and their IDs
# ==============================================================================
            """
            for accepted_chain in accepted_chains:
                out += "\n# " + accepted_chain + " : " + str(self.Name_To_ChainID(accepted_chain))
            raise Exception(out)
        else:
            self.chainId = self.Name_To_ChainID(chain)

        # Exchanges / Protocols
        if len(protocols) == 0:
            req = Request(url="https://api.1inch.exchange/v3.0/" + str(self.chainId) + "/protocols", headers=self.headers) 
            self.protocols = json.loads(urlopen(req).read())["protocols"]
        else:
            self.protocols = protocols
        
        # Tokens / Cryptocurrencies
        tokens = []
        req = Request(url="https://api.1inch.exchange/v4.0/" + str(self.chainId) + "/tokens", headers=self.headers) 
        token_reference = json.loads(urlopen(req).read())

        for key in token_reference["tokens"].keys():
            tokens.append(token_reference["tokens"][key]["symbol"])
        
        self.tokens = tokens
    
    ### Primary
    def Find(self, toToken, fromToken = "", amount = 1000):
        # Fixed toToken
        # One Path

        ### Set vars
        if fromToken == "":
            fromToken = self.tokens[0]
            print("\n# Assuming fromToken = " + fromToken)
            print("# toToken = " + toToken)
        else:
            print("\n# fromToken = " + fromToken)
            print("# toToken = " + toToken)


        ### Find Addresses
        toTokenAddress = self.Ticker_To_Address(toToken)
        fromTokenAddress = self.Ticker_To_Address(fromToken)

        ### Find Data Structure
        findData = {
            "toTokenAddress": toTokenAddress,
            "fromTokenAddress": fromTokenAddress,
            "amount": amount,
            "protocols": {
            },
            "final": {
                "highProtocol": {
                },
                "lowProtocol": {
                }
            },
            "estimatedProfit": None, # Accounting for stepped gas
        }

        ### Run Scripts
        findData = self.FindV1(findData)
        return findData

    def Buy(self, toToken):
        print("try me bitch")

    ### Secondary
    def Ticker_To_Address(self, token):
        req = Request(url="https://api.1inch.exchange/v4.0/" + str(self.chainId) + "/tokens", headers=self.headers) 
        token_reference = json.loads(urlopen(req).read())

        for key in token_reference["tokens"].keys():
            if token_reference["tokens"][key]["symbol"] == token:
                return token_reference["tokens"][key]["address"]
    
    def Name_To_ChainID(self, name):
        req = Request(url="https://chainid.network/chains_mini.json", headers=self.headers)
        Network_reference = json.loads(urlopen(req).read())

        for Chain_ref in Network_reference:
            if Chain_ref["name"] == name:
                return Chain_ref["chainId"]


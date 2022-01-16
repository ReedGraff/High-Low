import json
from datetime import datetime
import robin_stocks.robinhood as rs

def Gates(self, data):
    # This is going to have a set # of Gates... later in we will make it open to be changed...

    # Find type and run specified function
    type_data = data["parameters"][1]["Type"]
    print(type_data)
    

    if type_data == "Force Buy":
        Ticker = data["parameters"][0]["Ticker"]
        Amount = data["parameters"][1]["Amount"] # In dollars

        # Make the order
        #rs.orders.order_buy_fractional_by_price(Ticker, Amount, timeInForce='gtc') # If premium: add the parameter -> (, extendedHours=False)

        # Change data in transactions, and in the amount spent...
        file = open("Bot/Assets/Transactions.json", "r+")
        data = json.load(file)

        # Construct additional data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        additional_data = {
            "trade_number": len(data[self.name]["Transactions"]),
            "type": "Force Buy",
            "USD_value": Amount,
            "date-time": dt_string
        }

        # Append to data
        data[self.name]["Transactions"].append(additional_data)

        # Add to Current Amount Spent
        data[self.name]["Current Amount Spent"] += Amount

        # dump to Transaction file
        file.seek(0)
        json.dump(data, file, indent=4)


    elif type_data == "Force Sell":
        Ticker = data["parameters"][0]["Ticker"]
        Amount = data["parameters"][1]["Amount"] # In dollars

        # Make the order
        #rs.orders.order_sell_fractional_by_price(Ticker, Amount, timeInForce='gtc') # If premium: add the parameter -> (, extendedHours=False)

        # Change data in transactions, and in the amount spent...
        file = open("Bot/Assets/Transactions.json", "r+")
        data = json.load(file)

        # Construct additional data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        additional_data = {
            "trade_number": len(data[self.name]["Transactions"]),
            "type": "Force Sell",
            "USD_value": Amount,
            "date-time": dt_string
        }

        # Append to data
        data[self.name]["Transactions"].append(additional_data)

        # Add to Current Amount Spent
        data[self.name]["Current Amount Spent"] -= Amount

        # dump to Transaction file
        file.seek(0)
        json.dump(data, file, indent=4)


    if type_data == "Dynamic":
        Ticker = data["parameters"][0]["Ticker"]
        Amount = data["parameters"][1]["Amount"] # In dollars

        ### Actual Determination Start







        # Find 

        # Make the order
        #rs.orders.order_sell_fractional_by_price(Ticker, Amount, timeInForce='gtc') # If premium: add the parameter -> (, extendedHours=False)

        # Change data in transactions, and in the amount spent...
        file = open("Bot/Assets/Transactions.json", "r+")
        data = json.load(file)

        # Construct additional data
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        additional_data = {
            "trade_number": len(data[self.name]["Transactions"]),
            "type": "Dynamic",
            "USD_value": Amount,
            "date-time": dt_string
        }

        # Append to data
        data[self.name]["Transactions"].append(additional_data)

        # Add to Current Amount Spent
        data[self.name]["Current Amount Spent"] -= Amount

        # dump to Transaction file
        file.seek(0)
        json.dump(data, file, indent=4)
        """
        # Find Month
        date_format = "%m/%d/%Y"
        a = datetime.strptime('8/18/2008', date_format)
        b = datetime.strptime('9/26/2008', date_format)
        delta = b - a
        print delta.days # that's it
        """
        print("Not here yet")







        ### Actual Determination End














    # Print inputted data
    file = open("Bot/Assets/Random.json", "w+")
    json.dump(data, file, indent=4)


# Find the date nearest to a datetime
def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
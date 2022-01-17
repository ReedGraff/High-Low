import json
from datetime import datetime, timedelta
import robin_stocks.robinhood as rs

def Gates(self, data):
    # This is going to have a set # of Gates... later in we will make it open to be changed...

    # Find type and run specified function
    type_data = data["parameters"][1]["Type"]
    

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
        High = data["parameters"][1]["High"] # In dollars
        Low = data["parameters"][1]["Low"] # In dollars

        # Save inputted data
        file = open("Bot/Assets/Random.json", "w+")
        json.dump(data, file, indent=4)













        ### Actual Determination Start

        # Find today's date
        now = datetime.now()

        # Iterate and make all of the dates into datetime objects
        list_of_ticker_vals = list(data["parameters"][0].keys())[1:-1] # 1 (to avoid ticker), -1 (to avoid latest)

        for value in list_of_ticker_vals:
            data_list = data["parameters"][0][value]

            for value_object in data_list:
                date = value_object["begins_at"][:-1]
                value_object["begins_at"] = datetime.fromisoformat(date)
        


        # Make dictionary for easy viewing
        Gate_Watch = {
            "Ticker": Ticker
        }



        # Find the price a year ago: Year_Long
        year_date_list = [] 
        for value_object in data["parameters"][0]["Year_Long"]: # make a list of all of the dates in a year
            year_date_list.append(value_object["begins_at"])

        d = timedelta(days = 365) # find the date closest to 365 days ago...
        date_year_ago = now - d
        res = min(year_date_list, key=lambda sub: abs(sub - date_year_ago)) # find the date closest to 365 days ago...

        Year_Ago = data["parameters"][0]["Year_Long"][year_date_list.index(res)]["open_price"]
        
        Gate_Watch.update({ 
            "Year_Ago": float(Year_Ago) # update value to Gate_Watch
        })
        


        # Find the price a month ago: Month_Long
        month_date_list = [] 
        for value_object in data["parameters"][0]["Month_Long"]: # make a list of all of the dates in a year
            month_date_list.append(value_object["begins_at"])

        d = timedelta(days = 30) # find the date closest to 30 days ago...
        date_month_ago = now - d
        res = min(month_date_list, key=lambda sub: abs(sub - date_month_ago)) # find the date closest to 365 days ago...

        Month_Ago = data["parameters"][0]["Month_Long"][month_date_list.index(res)]["open_price"]
        
        Gate_Watch.update({ 
            "Month_Ago": float(Month_Ago) # update value to Gate_Watch
        })



        # Find the price a week ago: Week_Long
        week_date_list = [] 
        for value_object in data["parameters"][0]["Week_Long"]: # make a list of all of the dates in a year
            week_date_list.append(value_object["begins_at"])

        d = timedelta(days = 7) # find the date closest to 7 days ago...
        date_week_ago = now - d
        res = min(week_date_list, key=lambda sub: abs(sub - date_week_ago)) # find the date closest to 7 days ago...

        Week_Ago = data["parameters"][0]["Week_Long"][week_date_list.index(res)]["open_price"]
        
        Gate_Watch.update({ 
            "Week_Ago": float(Week_Ago) # update value to Gate_Watch
        })



        # Find the price a day ago: Day_Long
        day_date_list = [] 
        for value_object in data["parameters"][0]["Day_Long"]: # make a list of all of the dates in a year
            day_date_list.append(value_object["begins_at"])

        d = timedelta(days = 7) # find the date closest to 1 day ago...
        date_day_ago = now - d
        res = min(day_date_list, key=lambda sub: abs(sub - date_day_ago)) # find the date closest to 1 days ago...

        Day_Ago = data["parameters"][0]["Day_Long"][day_date_list.index(res)]["open_price"]
        
        Gate_Watch.update({ 
            "Day_Ago": float(Day_Ago) # update value to Gate_Watch
        })


        
        # Find the price an hour ago: Day_Long
        d = timedelta(hours = 1) # find the date closest to 1 hour ago...
        date_hour_ago = now - d
        res = min(day_date_list, key=lambda sub: abs(sub - date_hour_ago)) # find the date closest to 1 hour ago...

        Hour_Ago = data["parameters"][0]["Day_Long"][day_date_list.index(res)]["open_price"]
        
        Gate_Watch.update({ 
            "Hour_Ago": float(Hour_Ago) # update value to Gate_Watch
        })



        # Reference the current price: Latest
        Gate_Watch.update({ 
            "Current": float(data["parameters"][0]["Latest"][0]) # update value to Gate_Watch
        })



        # Make the order
        print(Gate_Watch)

        if all(i <= Gate_Watch["Current"] for i in list(Gate_Watch.values())[1:-2]): # -1 ignores the last hour and current
            if High == 0:
                # You have already spent the maximum amount
                print("You have already spent the maximum amount, and cannot buy more")
            
            else:
                # Buy the stock
                print("Buying stock")
                #rs.orders.order_sell_fractional_by_price(Ticker, Amount, timeInForce='gtc') # If premium: add the parameter -> (, extendedHours=False)

        else:
            if Low == 0:
                # You have already sold the maximum amount
                print("You have already sold the maximum amount, and cannot sell more")
            
            else:
                # Sell the stock
                print("Selling stock")
                #rs.orders.order_sell_fractional_by_price(Ticker, Amount, timeInForce='gtc') # If premium: add the parameter -> (, extendedHours=False)


        '''
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
        '''
        """
        # Find Month
        date_format = "%m/%d/%Y"
        a = datetime.strptime('8/18/2008', date_format)
        b = datetime.strptime('9/26/2008', date_format)
        delta = b - a
        print delta.days # that's it
        """
        #print("Not here yet")


        ### Actual Determination End
















# Find the date nearest to a datetime
def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
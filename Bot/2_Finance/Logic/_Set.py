import json

def Set(self, data):
    infinite = data["parameters"][1]
    
    if infinite:
        # You can charge "Amount" an infinite number of times
        Amount = data["parameters"][0]

        finance_data = {
            "Type": "Force Buy",
            "Amount": Amount
        }

    else:
        # You can charge "Amount", as long as you have not already spent that much...
        Allowance = data["parameters"][0]

        # Get the Current Amount Spent, to make sure that we stay within that range...
        file = open('Bot/Assets/Transactions.json')
        file_data = json.load(file)
        Current_Amount_Spent = file_data[self.name]["Current Amount Spent"]

        if Current_Amount_Spent > Allowance:
            # Managing spending too much...
            finance_data = {
                "Type": "Force Sell",
                "Amount": Current_Amount_Spent - Allowance
            }

        elif Current_Amount_Spent < 0:
            # If the current amount spent equal to or less than Allowance
            finance_data = {
                "Type": "Force Buy",
                "Amount": -Current_Amount_Spent
            }

        else:
            finance_data = {
                "Type": "Dynamic",
                "High": Allowance - Current_Amount_Spent, # Highest amount to be spent
                "Low": -Current_Amount_Spent # Highest amount to be sold
            }
        
    return finance_data
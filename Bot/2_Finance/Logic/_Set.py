def Set(self, data):
    infinite = data["parameters"][1]
    if infinite:
        # You can charge "Amount" an infinite number of times
        Amount = data["parameters"][0]
        return Amount

    else:
        # You can charge "Amount", as long as you have not already spent that much...
        file = open('Assets/Transactions.json')
        data = json.load(file)
        


        """
        with open("transactions.json", "w") as outfile:
            json.dump(sorted_data, outfile, indent=4)
        """
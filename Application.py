import Bot # This is the local Python Module that we made

# Initialization
bot_1 = Bot.Bot("ya boi", "just got bamboozled", "Bot_1")

# Find Functionality
find_input = {
    "function_name": "One_Stock",
    "parameters": [
        "FIS"
    ]
}
find_output = bot_1.Find(find_input)

# Finance Functionality
finance_input = {
    "function_name": "Set",
    "parameters": [
        10, # 10 dollars
        False # 10 dollars infinitely... If it was False, then it would be limited to 10 dollars 
    ]
}
"""
finance_input = {
    "function_name": "Set",
    "parameters": [
        10, # 10 dollars
        True # 10 dollars infinitely... If it was False, then it would be limited to 10 dollars 
    ]
}
"""
finance_output = bot_1.Finance(finance_input)

# Algorithm Functionality
algorithm_input = {
    "function_name": "Gates",
    "parameters": [
        find_output,
        finance_output
    ]
}
bot_1.Algorithm(algorithm_input)










"""
ways for this to work:

1.

import all functions in the beginning... and have the application.py file run the logic explicitely...

2.

import programmatically based on name... then allow json entry to decide the parameters of the other functions...


____

find fuctions return json...
finance fuctions return json...

algorithm function is in a while true loop that runs depending on:
- find json
- finance json
- any additionals parameters
... some algorithms will not need find json or finance json

"""
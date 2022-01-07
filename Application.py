import Bot # This is the local Python Module that we made



bot_1 = Bot.Bot("ya boi", "just got bamboozled")

find_input = {
    "function_name": "One_Stock",
    "parameters": [
        "Random stock name"
    ]
}

print(bot_1.Find(find_input))

#print(bot_1.Find_Function_Path("Find", "Value_Investing"))

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
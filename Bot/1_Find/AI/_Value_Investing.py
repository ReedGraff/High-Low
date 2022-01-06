def Value_Investing(self, training_data, testing_data=""):
    if testing_data == "":
        percent_taken = 30
        index = ((100 - percent_taken) / 100) * len(training_data)
        testing_data = training_data[index:]
    return 0
import robin_stocks.robinhood as rs

def One_Stock(self, data):   
    Ticker = data["parameters"][0]
    data.update({
        "Year_Long": rs.stocks.get_stock_historicals(Ticker, interval="day", span="5year"),
        "Year_Long": rs.stocks.get_stock_historicals(Ticker, interval="day", span="year"),
        "Month_Long": rs.stocks.get_stock_historicals(Ticker, interval="hour", span="month"),
        "Week_Long": rs.stocks.get_stock_historicals(Ticker, interval="hour", span="week"),
        "Day_Long": rs.stocks.get_stock_historicals(Ticker, interval="5minute", span="day")
    })
    return data

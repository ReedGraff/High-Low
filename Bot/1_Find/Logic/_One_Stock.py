import robin_stocks.robinhood as rs

def One_Stock(self, data):   
    Ticker = data["parameters"][0]
    new_data = {
        "Ticker": Ticker,
        "Year_Long": rs.stocks.get_stock_historicals(Ticker, interval="day", span="5year"),
        "Year_Long": rs.stocks.get_stock_historicals(Ticker, interval="day", span="year"),
        "Month_Long": rs.stocks.get_stock_historicals(Ticker, interval="hour", span="month"),
        "Week_Long": rs.stocks.get_stock_historicals(Ticker, interval="hour", span="week"),
        "Day_Long": rs.stocks.get_stock_historicals(Ticker, interval="5minute", span="day"),
        "Latest": rs.stocks.get_latest_price(Ticker)
    }
    return new_data

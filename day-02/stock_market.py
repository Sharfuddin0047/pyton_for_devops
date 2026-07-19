import requests

API_KEY = "QRHE86JT0WVBQLHI"
api_url = 'https://www.alphavantage.co/'



def get_stock_market_data(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    print(response.json())

symbol = input("Enter the symbol you want to check the stock eg {AMZN, IBM, GOGL}: ")
get_stock_market_data(symbol)
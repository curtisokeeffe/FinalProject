from flask import Flask, render_template, request, abort, redirect, url_for
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries  
from config import ALPHAVANTAGE_API_KEY
import json #was not used
import pandas as pd
#importing all necassary libraries and functions

app = Flask(__name__)
#initializing the flask app

def fetch_stock_data(symbol, range): #function to fetch stock data
    api_key = ALPHAVANTAGE_API_KEY #assigning hte API key to a variable
    ts = TimeSeries(key=api_key, output_format='pandas') #initializing the TimeSeries function from the alpha_vantage library

    try: #try block to catch any errors
        end_date = datetime.now()

        if range == '1d':
            # Intraday data for 1-day range with 5-minute intervals
            data, _ = ts.get_intraday(symbol=symbol, interval='5min', outputsize='full')
        elif range == '1w':
            # Intraday data for 1-week range with 2-hour intervals
            data, _ = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
        else:
            # Daily data for longer ranges
            data, _ = ts.get_daily(symbol=symbol, outputsize='full')

        current_price = data.iloc[0]['4. close'] #assigning the current price to a variable before reversing for accuracy
        data = data.iloc[::-1]  # Reverse the order for chronological order

        # Calculate the start date based on the range
        if range == '1d':
            start_date = end_date - timedelta(days=1)
        elif range == '1w':
            start_date = end_date - timedelta(weeks=1)
        elif range == '1m':
            start_date = end_date - timedelta(days=30)
        else:  # Default to 1 year
            start_date = end_date - timedelta(days=365)

        processed_data = data[(data.index >= start_date) & (data.index <= end_date)] #processing the data to get the data within the range

        if processed_data.empty: #if the data is empty, return None for all values
            return None, None, None, None 

        total_volume = processed_data.iloc[0].get('5. volume', 0) #assigning the total volume to a variable
        approximate_market_cap = "${:,.2f}".format(current_price * total_volume) #calculating the market cap for the given period

        dates = processed_data.index.strftime('%Y-%m-%d %H:%M:%S' if range in ['1d', '1w'] else '%Y-%m-%d').tolist() #assigning the dates to a variable
        closing_prices = processed_data['4. close'].tolist() #assigning the closing prices to a variable

    except Exception as e: #catching any errors
        print(f"Error fetching stock data for {symbol}: {e}") #printing the error if any
        return None, None, None, None
  
    return dates, closing_prices, current_price, approximate_market_cap #returning the values

@app.route('/') #route for the home page
def index():
    return render_template('index.html')    


#routes for each stock, see DrHortons route for general description of each line as all routes are basicall the same

@app.route('/DrHorton') #route for DrHorton
def drhorton(): #function for DrHorton
    range = request.args.get('range', default='1y') #assigning the range to a variable
    labels, values, current_price, market_cap = fetch_stock_data('DHI', range) #calling the fetch_stock_data function and assigning the values to variables
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))

    return render_template('drhorton.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap) #rendering the template with the values

@app.route('/Amazon')
def amazon():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('AMZN', range)
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))

    return render_template('amazon.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)

@app.route('/Microsoft')
def microsoft():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('MSFT', range)
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))
    
    print("Current Price:", current_price)  # Add this line to log the current price, this was for testing earlier on
    
    return render_template('microsoft.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)

@app.route('/Nvidia')
def nvidia():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('NVDA', range)
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))

    return render_template('nvidia.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)

@app.route('/MercadoLibre')
def mercadolibre():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('MELI', range)
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))

    return render_template('mercadolibre.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)

@app.route('/search') #route for the search page
def search():
    symbol = request.args.get('stock_symbol') #assigning the stock symbol to a variable
    if symbol: #if the symbol is not empty, redirect to the search result page
        return redirect(url_for('search_result', symbol=symbol)) 
    else:
        return "Please enter a stock symbol", 400 #else return an error


@app.route('/search_result/<symbol>') #route for the search result page
def search_result(symbol):
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data(symbol.upper(), range)
    
    if None in [labels, values, current_price, market_cap]:
        # Redirect to error page if any of the values are None
        return redirect(url_for('error'))

    
    return render_template('search_result.html', symbol=symbol, labels=labels, values=values, current_price=current_price, market_cap=market_cap)


@app.route('/error') #route for the error page
def error():
    
    return render_template('error.html')


if __name__ == '__main__': #running the app
    app.run(debug=True)


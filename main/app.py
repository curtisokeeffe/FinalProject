from flask import Flask, render_template, request
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries  


app = Flask(__name__)

def fetch_stock_data(symbol, range):
    api_key = 'V7A683AS9GWS1JFK'
    ts = TimeSeries(key=api_key, output_format='pandas')

    # Fetch data based on the range
    if range == '1y':
        data, _ = ts.get_daily(symbol=symbol, outputsize='full')
    elif range == '1m':
        data, _ = ts.get_daily(symbol=symbol, outputsize='compact')
        data = data.last('1M')  # Filter last 1 month
    elif range == '1w':
        data, _ = ts.get_daily(symbol=symbol, outputsize='compact')
        data = data.last('7D')  # Filter last 7 days
    elif range == '1d':
        data, _ = ts.get_intraday(symbol=symbol, interval='5min')
        data = data.last('1D')  # Filter last 1 day

    try:
        # Extract current price and total volume
        latest_data = data.iloc[-1]
        current_price = latest_data['4. close']
        total_volume = latest_data['5. volume']
        approximate_market_cap = current_price * total_volume
    except Exception as e:
        current_price = total_volume = approximate_market_cap = None
        print(f"Error calculating stock data: {e}")

    # Prepare dates and closing prices
    dates = data.index.strftime('%Y-%m-%d').tolist()
    closing_prices = data['4. close'].tolist()

    return dates, closing_prices, current_price, approximate_market_cap

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/DrHorton')
def drhorton():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('DHI', range)
    return render_template('drhorton.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)


@app.route('/Amazon')
def amazon():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('AMZN', range)
    return render_template('amazon.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)


@app.route('/MercadoLibre')
def mercadolibre():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('MELI', range)
    return render_template('mercadolibre.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)


@app.route('/Microsoft')
def microsoft():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('MSFT', range)
    return render_template('microsoft.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)


@app.route('/Nvidia')
def nvidia():
    range = request.args.get('range', default='1y')
    labels, values, current_price, market_cap = fetch_stock_data('NVDA', range)
    return render_template('nvidia.html', labels=labels, values=values, current_price=current_price, market_cap=market_cap)


if __name__ == '__main__':
    app.run(debug=True)


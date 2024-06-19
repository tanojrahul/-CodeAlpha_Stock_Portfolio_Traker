# -CodeAlpha_Stock_Portfolio_Traker



# Portfolio Tracker

This Python script allows users to track a stock portfolio by retrieving real-time stock quotes, managing buy/sell transactions, and displaying the overall portfolio performance using the Finnhub API.

## Features

- **View current stock price**: Retrieve and display the current, open, high, and low prices of a stock.
- **Portfolio tracking**: Continuously update and display the total profit/loss, buy price, and current price of the portfolio.
- **Buy stocks**: Add stock positions to the portfolio.
- **Sell stocks**: Remove stock positions from the portfolio and calculate profit/loss.
- **Symbol search**: Look up stock symbols and retrieve information.
- **Market status**: Check the current market status for the US exchange.
- **Recommendation trends**: Retrieve and display recommendation trends for a given stock.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/portfolio-tracker.git
    cd portfolio-tracker
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install finnhub-python
    ```

4. Set up your Finnhub API key:

    Replace `"Your Api key"` in the code with your actual Finnhub API key.

## Usage

Run the script:

```bash
python main.py
```

You will be presented with a menu with the following options:

1. View Portfolio
2. Buy
3. Sell
4. View Symbols
5. Market Status
6. Recommendation Trends
7. Exit

### Menu Options

- **View Portfolio**: Displays the total profit/loss, buy price, current price, and individual positions.
- **Buy**: Prompts for a stock symbol and quantity to add to the portfolio.
- **Sell**: Prompts for a stock symbol and quantity to remove from the portfolio.
- **View Symbols**: Prompts for a symbol or name to search and display matching stock symbols.
- **Market Status**: Displays the current market status for the US exchange.
- **Recommendation Trends**: Prompts for a stock symbol and displays its recommendation trends.
- **Exit**: Exits the program.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.



## Acknowledgements

- [Finnhub API](https://finnhub.io/docs/api) for providing stock market data.

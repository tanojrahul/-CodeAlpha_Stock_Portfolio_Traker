import os

import finnhub
import time

finnhub_client = finnhub.Client(api_key="Your Api key")
data=finnhub_client.quote('AAPL')
print("Current price of AAPL:",data)
total=0
buy_price=0
positions={}
#symbol: (quantity,buy_price,current_price,PL)

def display(symbol):
    data = finnhub_client.quote(symbol)
    print("Current price:",data['c'])
    print("Open price:",data['o'])
    print("day high price:",data['h'])
    print("day low price:",data['l'])
    print("difference price:",data['d'])
    print("difference percentage:",data['dp'])

# display('AAPL')

def portfolio():
    while True:
        total,buy_price,current_price=update()
        print("______________________________________________________________________________")
        print(f" P/L : {total}     Buy Price: {buy_price}   Current Price: {current_price}")
        print("______________________________________________________________________________")

        print("Current Positions: ")
        positions_display()
        print("Wait 2 seconds !")
        time.sleep(2)
        c=input("Enter any key to exit!")
        if c:
            break
    os.system('cls')


def positions_display():
    print("Symbol      Quantity     Buy Price      Current Price      P/L: ")
    for keys in positions:
        print(f"{keys}      {positions[keys][0]}     {positions[keys][1]}     {positions[keys][2]}      {positions[keys][3]} ")


def buy(symbol,quantity):
    data = finnhub_client.quote(symbol)
    if symbol not in positions.keys():
        positions[symbol]=[quantity,data['c']*quantity,0,0]
    else:
        positions[symbol][0]+=quantity
        positions[symbol][1] += data['c']*quantity

        print("Successfully modified your order!")


def sell(symbol,quantity):
    if symbol not in positions.keys():
        print("you have no current positions for that symbol! :",symbol)
    else:
        positions[symbol][0] -= quantity
        positions[symbol][1] -=  (positions[symbol][1]/positions[symbol][0]) * quantity
        print("Your total Profit / Loss:",(positions[symbol][2]*positions[symbol][0])-(positions[symbol][1]*positions[symbol][0]))




def update():
    total=0
    buy_price=0
    current_price=0
    for key in positions:
        data = finnhub_client.quote(key)
        positions[key][2]=positions[key][0]*data['c']
        positions[key][3]=positions[key][0]*data['c']-positions[key][1]
        total+=positions[key][3]
        buy_price+=positions[key][1]
        current_price+=positions[key][2]
    return total,buy_price,current_price
def symbols():
    name=input("Enter an symbol or name to search: ")
    data=finnhub_client.symbol_lookup(name)

    for i in range(len(data['result'])):
        d = data['result'][i].items()
        for j in d:
            print(j[0], ":", j[1])
        print("-----------------------------\n")


# symbols()
def market_status():
    print(finnhub_client.market_status(exchange='US'))

def Recomendation_Trends(symbol):
    data=finnhub_client.recommendation_trends(symbol)
    d = data[0].items()
    for i in d:
        print(i[0], ":", i[1])

def menu():
    while True:
        print("\nMenu:")
        print("1. View Portfolio")
        print("2. Buy")
        print("3. Sell")
        print("4. View Symbols")
        print("5. Market Status")
        print("6. Recommendation Trends")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            portfolio()
        elif choice == '2':
            symbol = input("Enter symbol: ")
            quantity = int(input("Enter quantity: "))
            buy(symbol, quantity)
        elif choice == '3':
            symbol = input("Enter symbol: ")
            quantity = int(input("Enter quantity: "))
            sell(symbol, quantity)
        elif choice == '4':
            symbols()
        elif choice == '5':
            market_status()
        elif choice == '6':
            symbol = input("Enter symbol: ")
            Recomendation_Trends(symbol)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    pass
menu()


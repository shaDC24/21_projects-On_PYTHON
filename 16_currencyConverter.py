from requests import get
from pprint  import PrettyPrinter

API_KEY="562ddaf40c95f5d58108"
BASE_URL="https://free.currconv.com/"
#BASE_URL="https://api.freecurrencyapi.com/"
# https://api.freecurrencyapi.com/v1/status?apikey=fca_live_7Mwfglh2iZU6E1HIedO8iVttCRKPse9r36VBhWtt

printer=PrettyPrinter()

def get_currencies():
    endpoint=f"api/v7/currencies?apiKey={API_KEY}"
    url=BASE_URL+endpoint
    data=get(url).json() #['results']
    data=list(data.items())
    data.sort()
    printer.pprint(data)
    return data



def print_Currencies(currencies):
    for currency in currencies:
        name=currency['name']
        _id=currency['id']
        symbol=currency.get('currencySymbol',"")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1,currency2):
    endpoint=f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url=BASE_URL+endpoint
    response=get(url)
    data=response.json()
    if len(data)==0 :
        print("Invalid Currencies.")
        return
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate
    

def convert(currency1,currency2,amount):
    rate=exchange_rate(currency1,currency2)
    if rate is None:
        return
    try:
        amount=float(amount)
    except:
        print("Invalid amount.")
        return  
    converted_amount=rate*amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount



def main():
    currencies=get_currencies()
    print("Welcome to currency converter.")
    print("L - lists the different currencies.")
    print("C - convert from one currency to another")
    print("R - get the exchange rate of two currencies.")
    print()
    while(True):
        command=input("Enter a command (q to quit) : ").lower()
        if command=="q": break
        
        elif command=="l":
            print_Currencies(currencies)
        
        elif command=="c":
            currency1=input("Enter a base currency : ").upper()
            currency2=input("Enter a currency to convert to : ").upper()
            amount=input(f"Enter an amount in {currency1} : ")
            convert(currency1,currency2,amount)
        
        elif command=="r":
            currency1=input("Enter a base currency : ").upper()
            currency2=input("Enter a currency to convert to : ").upper()
            exchange_rate(currency1,currency2)
        
        else:
            print("Unrecognized command..! :::((((()))))")
            
            
            
main()



import requests
from pprint import PrettyPrinter
API_KEY = ""
url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=AED&amount=1000"

BASE_URL = "https://api.apilayer.com/"

payload = {}
headers = {
    "apiKey": API_KEY
}

printer = PrettyPrinter(4)

def get_available_currencies():
    endpoint = "exchangerates_data/symbols"
    
    response = requests.request("GET", BASE_URL + endpoint, headers=headers, data=payload)
    
    if response.status_code == 200:
        printer.pprint(response.json()["symbols"])
        
    else:
        print("Somthing wrong, please try again later!")

def covnert():
    currency1 = input("Enter base currency: ").upper()
    currency2 = input("Enter currency convert to: ").upper()
    amount = input("Enter amount to convert: ")
    
    endpoint = f"exchangerates_data/convert?to={currency1}&from={currency2}&amount={amount}"
    
    response = requests.request("GET", BASE_URL + endpoint, headers=headers, data=payload)
    
    if response.status_code == 200:
        data = response.json()
        print(f"{amount} {currency1} = {data['result']} {currency2}")
    else:
        print("Something went wrong, please try again later!")
        
        
def main():
    print("Welcome to exchange app!")
    print("Enter list -> get list of available currencies.")
    print("Enter convert -> convet amount from currency to another.")
    print("Enter q -> to quite the program")

    while True:
        command = input("Enter your command: ").lower()
        if command == "q":
            quit()
        elif command == "list":
            get_available_currencies()
        elif command == "convert":
            covnert()



main()
